"""Private attachment-corpus reanalysis without retaining article text.

The functions in this module are intentionally conservative. They verify local
PDFs by checksum, extract text without OCR through ``textio.read_text``, compute
only derived abstract/prose measurements, and never place article text in the
returned payload.
"""

from __future__ import annotations

from collections import Counter
import csv
import json
from pathlib import Path
import re
from typing import Any, Iterable, Mapping

from .corpus import sha256_file
from .metrics import aggregate_metrics, analyze_text, clean_prose
from .textio import read_text

ABSTRACT_START_RE = re.compile(
    r"(?im)(?:^|\n)\s*(?:abstract|a\s*b\s*s\s*t\s*r\s*a\s*c\s*t)\s*(?:[—–\-:.]|\s)*"
)
ABSTRACT_END_RE = re.compile(
    r"(?im)(?:\n\s*(?:index\s+terms?|key\s*words?)\s*(?:[—–\-:.]|\s)*"
    r"|\n\s*(?:(?:i|1)\s*[.\-:]?\s*)?(?:introduction|i\s*n\s*t\s*r\s*o\s*d\s*u\s*c\s*t\s*i\s*o\s*n)\b)"
)

_METADATA_START_RE = re.compile(
    r"(?i)^(?:received\b|manuscript received\b|[∗*]\s*corresponding author\b|corresponding author\b)"
)
_METADATA_END_RE = re.compile(
    r"(?i)(?:digital object identifier|doi\.org/|all rights reserved|open access article|published by|©|copyright)"
)
_METADATA_LINE_RE = re.compile(
    r"(?i)(?:authorized licensed use|personal use is permitted|republication/redistribution|"
    r"e-?mail(?: addresses?)?\s*:|school of |college of |department of |university[, ]|"
    r"available online at|journal homepage|contents lists available|supplementary downloadable material)"
)
_AUTHOR_LINE_RE = re.compile(
    r"^(?:[A-Z]\.-[A-Z]\.\s+[A-Z][A-Za-z-]+|[A-Z]\.\s+[A-Z][A-Za-z-]+(?:\s+\([A-Z]\))?)$"
)


def _clean_abstract_candidate(candidate: str) -> str:
    """Remove common front-page metadata intrusions from an abstract candidate."""

    lines = candidate.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    kept: list[str] = []
    in_metadata = False
    metadata_has_end = False
    prose_words_kept = 0
    for raw in lines:
        line = re.sub(r"\s+", " ", raw).strip()
        if not in_metadata and _METADATA_START_RE.search(line):
            # A Received line in publisher front matter can precede an unlabeled
            # abstract in the same extracted block. Only enter block-skip mode
            # after substantial abstract prose has already been retained.
            if prose_words_kept >= 50:
                in_metadata = True
                metadata_has_end = bool(_METADATA_END_RE.search(line))
            continue
        if in_metadata:
            if _METADATA_END_RE.search(line):
                metadata_has_end = True
            if metadata_has_end and not line:
                in_metadata = False
                metadata_has_end = False
            continue
        if not line:
            kept.append("")
            continue
        if _METADATA_LINE_RE.search(line):
            continue
        if _AUTHOR_LINE_RE.fullmatch(line):
            continue
        if re.fullmatch(r"[0-9]+", line):
            continue
        if re.search(r"(?i)https?://(?:dx\.)?doi\.org/", line):
            continue
        if re.search(r"(?i)(?:\bvol\.\s*\d+|transactions on|journal of the|nonlinear dyn)" , line) and len(line.split()) < 18:
            continue
        if re.search(r"(?i)(?:©|copyright|all rights reserved|published by)", line):
            continue
        kept.append(line)
        prose_words_kept += len(re.findall(r"[A-Za-z]+(?:[-'][A-Za-z]+)*|\d+(?:\.\d+)?", line))
    prose = clean_prose("\n".join(kept))
    # Guard against a layout failure that swallowed multiple pages.
    if len(prose.split()) > 800:
        prose = " ".join(prose.split()[:800])
    return prose.strip()


ABSTRACT_MOVE_PATTERNS: dict[str, tuple[str, ...]] = {
    "context_stakes": (
        "security",
        "cyber",
        "network",
        "malware",
        "attack",
        "propaganda",
        "rumor",
        "social engineering",
    ),
    "gap_limitation": (
        "however",
        "remain",
        "lack",
        "limited",
        "challenge",
        "has not",
        "have not",
    ),
    "model_framework": (
        "model",
        "framework",
        "approach",
        "system",
        "mechanism",
    ),
    "decision_problem": (
        "optimal control",
        "differential game",
        "impulse control",
        "optimization problem",
        "nash",
        "stackelberg",
        "policy",
        "strategy",
    ),
    "theory_conditions": (
        "theorem",
        "necessary condition",
        "optimality system",
        "equilibrium",
        "stability",
        "threshold",
        "derive",
        "establish",
    ),
    "algorithm_solver": (
        "algorithm",
        "solver",
        "forward-backward",
        "iterative",
        "reinforcement learning",
        "pinn",
        "pidl",
    ),
    "evaluation": (
        "experiment",
        "simulation",
        "numerical",
        "dataset",
        "network topology",
        "real-world network",
        "synthetic network",
    ),
    "result_claim": (
        "results show",
        "results indicate",
        "results demonstrate",
        "experiments show",
        "experiments demonstrate",
        "outperform",
        "reduce",
        "improve",
    ),
    "implication": (
        "insight",
        "guidance",
        "implication",
        "cost-effective",
        "decision-making",
        "practical",
    ),
}


def extract_abstract(text: str) -> str:
    """Extract a best-effort abstract from text without returning surrounding prose."""

    normalized = text.replace("\r\n", "\n").replace("\r", "\n")
    # Abstracts should occur near the front matter. Limiting the search avoids a
    # table-of-contents or reference-list false match in long PDFs.
    front = normalized[:30_000]
    start_match = ABSTRACT_START_RE.search(front)
    if start_match:
        remainder = front[start_match.end() :]
        end_match = ABSTRACT_END_RE.search(remainder)
        candidate = remainder[: end_match.start()] if end_match else remainder[:5_000]
        return _clean_abstract_candidate(candidate)

    # Some venues print the abstract directly below the title without an
    # ``Abstract`` heading. In that case, take the final front-matter block
    # before Keywords or Introduction and clean author/affiliation metadata.
    end_match = ABSTRACT_END_RE.search(front)
    if not end_match:
        return ""
    prefix = front[: end_match.start()]
    paragraphs = [part for part in re.split(r"\n\s*\n", prefix) if part.strip()]
    for part in reversed(paragraphs):
        cleaned = _clean_abstract_candidate(part)
        count = len(cleaned.split())
        if 50 <= count <= 800 and re.search(r"[.!?]", cleaned):
            return cleaned

    # Layout extraction may collapse title, author and abstract into one block.
    cleaned = _clean_abstract_candidate(prefix[-6_000:])
    return cleaned if 50 <= len(cleaned.split()) <= 800 else ""


def detect_abstract_moves(abstract: str) -> list[str]:
    """Return coarse rhetorical moves from an abstract, never article excerpts."""

    lowered = abstract.lower()
    moves = []
    for move, patterns in ABSTRACT_MOVE_PATTERNS.items():
        if any(pattern in lowered for pattern in patterns):
            moves.append(move)
    return moves


def _safe_int(value: Any) -> int:
    try:
        return int(float(str(value).strip()))
    except (TypeError, ValueError):
        return 0


def _safe_float(value: Any, default: float = 1.0) -> float:
    try:
        result = float(str(value).strip())
    except (TypeError, ValueError):
        return default
    return result if result > 0 else default


def load_attachment_manifest(path: str | Path) -> list[dict[str, str]]:
    with Path(path).open(newline="", encoding="utf-8-sig") as handle:
        return [
            {key: (value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(handle)
        ]


def analyze_extracted_document(row: Mapping[str, str], text: str) -> dict[str, Any]:
    """Analyze one already-extracted article without placing source text in output."""

    abstract = extract_abstract(text)
    metrics = analyze_text(abstract, source=row.get("paper_id", ""), include_sections=False)
    tracked_words = _safe_int(row.get("abstract_words"))
    tracked_sentences = _safe_int(row.get("abstract_sentences"))
    return {
        "paper_id": row.get("paper_id", ""),
        "year": _safe_int(row.get("year")),
        "style_tier": row.get("style_tier", ""),
        "style_weight": _safe_float(row.get("style_weight"), 1.0),
        "is_ieee_transactions": row.get("is_ieee_transactions", "").lower() == "yes",
        "abstract_detected": bool(abstract),
        "extracted_text_words": len(clean_prose(text).split()),
        "derived_abstract_metrics": metrics,
        "tracked_abstract_words": tracked_words,
        "tracked_abstract_sentences": tracked_sentences,
        "abstract_word_delta": int(metrics.get("words", 0)) - tracked_words,
        "abstract_sentence_delta": int(metrics.get("sentences", 0)) - tracked_sentences,
        "abstract_moves": detect_abstract_moves(abstract),
    }


def _find_pdf_hashes(directory: Path) -> dict[str, list[Path]]:
    mapping: dict[str, list[Path]] = {}
    for path in sorted(directory.rglob("*.pdf")):
        digest = sha256_file(path)
        mapping.setdefault(digest, []).append(path)
    return mapping


def _aggregate_subset(items: Iterable[Mapping[str, Any]]) -> dict[str, Any]:
    weighted: list[tuple[Mapping[str, Any], float]] = []
    count = 0
    for item in items:
        if not item.get("abstract_detected"):
            continue
        metrics = item.get("derived_abstract_metrics", {})
        if not isinstance(metrics, Mapping):
            continue
        weighted.append((metrics, float(item.get("style_weight", 1.0))))
        count += 1
    aggregate = aggregate_metrics(weighted)
    aggregate["papers_with_detected_abstract"] = count
    return aggregate


def analyze_private_attachment_corpus(
    directory: str | Path,
    manifest_path: str | Path,
    *,
    max_word_delta: int = 40,
    max_sentence_delta: int = 5,
) -> dict[str, Any]:
    """Re-analyze a private PDF directory and return derived-only audit data."""

    directory = Path(directory).resolve()
    manifest_path = Path(manifest_path).resolve()
    if not directory.is_dir():
        raise FileNotFoundError(f"Private corpus directory does not exist: {directory}")
    rows = load_attachment_manifest(manifest_path)
    files_by_hash = _find_pdf_hashes(directory)
    expected_hashes = {(row.get("sha256") or "").lower(): row for row in rows}

    documents: list[dict[str, Any]] = []
    missing: list[dict[str, str]] = []
    extraction_failures: list[dict[str, str]] = []
    drift: list[dict[str, Any]] = []

    for digest, row in expected_hashes.items():
        matches = files_by_hash.get(digest, [])
        if not matches:
            missing.append(
                {
                    "paper_id": row.get("paper_id", ""),
                    "sha256": digest,
                    "source_filename_hint": row.get("source_filename_hint", ""),
                }
            )
            continue
        path = matches[0]
        try:
            text = read_text(path)
            derived = analyze_extracted_document(row, text)
        except Exception as exc:  # optional PDF dependency/parser failures must be reported
            extraction_failures.append(
                {
                    "paper_id": row.get("paper_id", ""),
                    "file": str(path.relative_to(directory)),
                    "error": f"{type(exc).__name__}: {exc}",
                }
            )
            continue
        derived["file"] = str(path.relative_to(directory))
        derived["sha256"] = digest
        documents.append(derived)
        if (
            abs(int(derived["abstract_word_delta"])) > max_word_delta
            or abs(int(derived["abstract_sentence_delta"])) > max_sentence_delta
            or not derived["abstract_detected"]
        ):
            drift.append(
                {
                    "paper_id": derived["paper_id"],
                    "abstract_detected": derived["abstract_detected"],
                    "abstract_word_delta": derived["abstract_word_delta"],
                    "abstract_sentence_delta": derived["abstract_sentence_delta"],
                }
            )

    unexpected = [
        {
            "sha256": digest,
            "files": [str(path.relative_to(directory)) for path in paths],
        }
        for digest, paths in files_by_hash.items()
        if digest not in expected_hashes
    ]
    duplicates = [
        {
            "sha256": digest,
            "files": [str(path.relative_to(directory)) for path in paths],
        }
        for digest, paths in files_by_hash.items()
        if len(paths) > 1
    ]

    core = [item for item in documents if item.get("style_tier") == "A_core_voice"]
    transactions = [item for item in documents if item.get("is_ieee_transactions")]
    recent = [item for item in documents if int(item.get("year", 0)) >= 2024]
    move_counts: Counter[str] = Counter()
    for item in documents:
        move_counts.update(item.get("abstract_moves", []))

    return {
        "schema_version": 1,
        "privacy_boundary": {
            "article_text_in_output": False,
            "ocr_used": False,
            "source_paths_absolute_in_output": False,
        },
        "manifest": str(manifest_path.name),
        "directory_label": directory.name,
        "expected_rows": len(rows),
        "pdf_files": sum(len(paths) for paths in files_by_hash.values()),
        "analyzed_documents": len(documents),
        "missing_rows": missing,
        "unexpected_hashes": unexpected,
        "duplicate_hashes": duplicates,
        "extraction_failures": extraction_failures,
        "metric_drift": drift,
        "thresholds": {
            "max_absolute_abstract_word_delta": max_word_delta,
            "max_absolute_abstract_sentence_delta": max_sentence_delta,
        },
        "counts": {
            "core_voice_documents": len(core),
            "ieee_transactions_documents": len(transactions),
            "recent_2024_plus_documents": len(recent),
        },
        "aggregates": {
            "all_attachment": _aggregate_subset(documents),
            "core_voice": _aggregate_subset(core),
            "ieee_transactions": _aggregate_subset(transactions),
            "recent_2024_plus": _aggregate_subset(recent),
        },
        "abstract_move_document_frequency": dict(sorted(move_counts.items())),
        "documents": documents,
        "complete_exact_hash_match": not missing and not unexpected and not duplicates,
        "analysis_complete": not missing and not unexpected and not duplicates and not extraction_failures,
        "tracked_metric_reproduction_within_tolerance": not drift,
        "note": (
            "PDF extraction and front-matter layout can change sentence/word counts. "
            "Investigate drift; do not silently overwrite tracked metrics."
        ),
    }


def write_private_corpus_audit(path: str | Path, payload: Mapping[str, Any]) -> Path:
    output = Path(path)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return output
