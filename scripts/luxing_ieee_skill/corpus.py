"""Publication-manifest and corpus-coverage utilities."""

from __future__ import annotations

from collections import Counter
import csv
import hashlib
from dataclasses import dataclass
from pathlib import Path
import re
from typing import Iterable
from urllib.parse import quote


@dataclass
class PublicationRecord:
    data: dict[str, str]

    @property
    def paper_id(self) -> str:
        return self.data.get("paper_id", "")

    @property
    def title(self) -> str:
        return self.data.get("title", "")

    @property
    def doi(self) -> str:
        return normalize_doi(self.data.get("doi", ""))

    @property
    def style_eligible(self) -> bool:
        return self.data.get("style_eligible", "").lower().startswith("yes")

    @property
    def fulltext_checked(self) -> bool:
        return self.data.get("fulltext_status", "").lower() in {"seed_analyzed", "attachment_analyzed", "analyzed", "checked"}


def normalize_doi(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)
    return value.rstrip(".,; ")


def normalize_title(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def load_manifest(path: str | Path) -> list[PublicationRecord]:
    p = Path(path)
    with p.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        return [PublicationRecord({key: (value or "").strip() for key, value in row.items()}) for row in reader]


def validate_manifest(records: Iterable[PublicationRecord]) -> list[str]:
    records = list(records)
    errors: list[str] = []
    ids: Counter[str] = Counter(record.paper_id for record in records)
    titles: Counter[str] = Counter(normalize_title(record.title) for record in records)
    dois: Counter[str] = Counter(record.doi for record in records if record.doi)

    for paper_id, count in ids.items():
        if not paper_id:
            errors.append("A manifest row has no paper_id.")
        elif count > 1:
            errors.append(f"Duplicate paper_id: {paper_id}")
    for title, count in titles.items():
        if not title:
            errors.append("A manifest row has no title.")
        elif count > 1:
            errors.append(f"Duplicate normalized title: {title}")
    for doi, count in dois.items():
        if count > 1:
            errors.append(f"Duplicate DOI: {doi}")
    for record in records:
        year = record.data.get("year", "")
        if year and not re.fullmatch(r"\d{4}", year):
            errors.append(f"Invalid year for {record.paper_id}: {year}")
        if record.data.get("style_eligible", "") and not record.data.get("role_confidence", ""):
            errors.append(f"Missing role_confidence for {record.paper_id}")
    return errors


def coverage_summary(records: Iterable[PublicationRecord]) -> dict[str, object]:
    records = list(records)
    eligible = [record for record in records if record.style_eligible]
    checked = [record for record in eligible if record.fulltext_checked]
    venues = Counter(record.data.get("venue", "unknown") for record in records)
    years = Counter(record.data.get("year", "unknown") for record in records)
    return {
        "records": len(records),
        "style_eligible": len(eligible),
        "fulltext_checked_style_eligible": len(checked),
        "fulltext_coverage_pct": round(100 * len(checked) / len(eligible), 2) if eligible else 0.0,
        "venues": dict(sorted(venues.items())),
        "years": dict(sorted(years.items())),
        "status": (
            "attachment-key-corpus-calibrated"
            if len(checked) < len(eligible)
            else "owner-priority-selected-fulltext-complete"
        ),
    }


def build_queue(records: Iterable[PublicationRecord], include_checked: bool = False) -> list[dict[str, str]]:
    queue = []
    for record in records:
        if not record.style_eligible:
            continue
        if record.fulltext_checked and not include_checked:
            continue
        doi = record.doi
        target = f"https://doi.org/{doi}" if doi else ""
        queue.append(
            {
                "paper_id": record.paper_id,
                "title": record.title,
                "year": record.data.get("year", ""),
                "venue": record.data.get("venue", ""),
                "doi": doi,
                "publisher_or_doi_url": target,
                "deakin_proxy_url": make_deakin_proxy_url(target) if target else "",
                "role_confidence": record.data.get("role_confidence", ""),
                "fulltext_status": record.data.get("fulltext_status", ""),
                "status": "pending",
            }
        )
    return sorted(queue, key=lambda item: (-int(item["year"] or 0), item["paper_id"]))


def write_queue(path: str | Path, rows: Iterable[dict[str, str]]) -> None:
    rows = list(rows)
    fields = [
        "paper_id",
        "title",
        "year",
        "venue",
        "doi",
        "publisher_or_doi_url",
        "deakin_proxy_url",
        "role_confidence",
        "fulltext_status",
        "status",
    ]
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def make_deakin_proxy_url(target_url: str) -> str:
    if not target_url:
        raise ValueError("A target URL is required.")
    return "https://ezproxy.deakin.edu.au/login?qurl=" + quote(target_url, safe="")


def sha256_file(path: str | Path) -> str:
    """Return a file SHA-256 without loading the whole file into memory."""

    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_local_attachment_corpus(
    directory: str | Path,
    manifest_path: str | Path,
) -> dict[str, object]:
    """Match private PDF files to the tracked attachment manifest by SHA-256.

    The function does not copy, parse, or modify article files. It reports
    checksum matches, missing manifest rows, duplicates, and unexpected PDFs.
    """

    directory = Path(directory)
    manifest_path = Path(manifest_path)
    if not directory.exists() or not directory.is_dir():
        raise FileNotFoundError(f"Private corpus directory does not exist: {directory}")
    with manifest_path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    expected_by_hash = {
        (row.get("sha256") or "").strip().lower(): row
        for row in rows
        if (row.get("sha256") or "").strip()
    }
    files = sorted(
        path for path in directory.rglob("*") if path.is_file() and path.suffix.lower() == ".pdf"
    )
    actual: dict[str, list[str]] = {}
    for path in files:
        digest = sha256_file(path)
        actual.setdefault(digest, []).append(str(path.relative_to(directory)))

    matched = []
    missing = []
    for digest, row in expected_by_hash.items():
        if digest in actual:
            matched.append(
                {
                    "paper_id": row.get("paper_id", ""),
                    "title": row.get("title", ""),
                    "sha256": digest,
                    "files": actual[digest],
                }
            )
        else:
            missing.append(
                {
                    "paper_id": row.get("paper_id", ""),
                    "title": row.get("title", ""),
                    "sha256": digest,
                    "source_filename_hint": row.get("source_filename_hint", ""),
                }
            )

    unexpected = [
        {"sha256": digest, "files": paths}
        for digest, paths in actual.items()
        if digest not in expected_by_hash
    ]
    duplicates = [
        {"sha256": digest, "files": paths}
        for digest, paths in actual.items()
        if len(paths) > 1
    ]
    return {
        "manifest": str(manifest_path),
        "directory": str(directory),
        "expected_rows": len(expected_by_hash),
        "pdf_files": len(files),
        "matched_rows": len(matched),
        "missing_rows": len(missing),
        "unexpected_hashes": len(unexpected),
        "duplicate_hashes": len(duplicates),
        "matched": matched,
        "missing": missing,
        "unexpected": unexpected,
        "duplicates": duplicates,
        "complete_exact_match": not missing and not unexpected and not duplicates,
        "note": (
            "A checksum mismatch can reflect a legitimate author-manuscript or publisher-version "
            "difference and requires manual version resolution."
        ),
    }
