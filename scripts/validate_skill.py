#!/usr/bin/env python3
"""Validate the installed personal skill without external dependencies."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
import re
import sys
import tempfile


sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
NAME = "luxing-ieee-transactions"

REQUIRED = (
    ".gitignore",
    "SKILL.md",
    "agents/openai.yaml",
    "references/PERSONAL_RESEARCH_DIRECTIONS.md",
    "references/PERSONAL_STYLE_PROFILE.md",
    "references/PERSONAL_STYLE_PROFILE.yaml",
    "references/FULLTEXT_CORPUS_DERIVED_DOCTRINE.md",
    "references/QUALITY_GATES.md",
    "references/CLAIM_LANGUAGE_RULES.yaml",
    "references/EVIDENCE_TRACKS.md",
    "references/TOPOLOGY_FIRST_EXPERIMENT_PROTOCOL.md",
    "references/RESEARCH_PIPELINE.md",
    "references/corpus/publication_manifest.csv",
    "references/corpus/local_attachment_manifest.csv",
    "references/corpus/local_corpus_metrics.json",
    "references/corpus/open_access_fulltext_manifest.csv",
    "references/corpus/expanded_fulltext_corpus_summary.json",
    "references/repo-family/repository_manifest.yaml",
    "assets/templates/PROJECT_CONFIG.yaml",
    "assets/templates/EVIDENCE_PLAN.json",
    "assets/templates/TOPOLOGY_CARD.yaml",
    "assets/templates/CROSS_PAPER_CONSISTENCY_LEDGER.csv",
    "scripts/luxing_ieee.py",
    "scripts/luxing_ieee_skill/cli.py",
    "tests/test_linter.py",
)

FORBIDDEN_SUFFIXES = {
    ".pdf", ".doc", ".docx", ".ppt", ".pptx", ".key", ".pages",
    ".pcap", ".pcapng", ".ckpt", ".pt", ".pth", ".zip", ".pyc",
}

FORBIDDEN_PARTS = {
    "private",
    "raw",
    "checkpoints",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    ".mypy_cache",
}


def _frontmatter(text: str) -> tuple[dict[str, str], list[str]]:
    errors: list[str] = []
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        return {}, ["SKILL.md must begin with YAML frontmatter."]
    block = text[4:].split("\n---\n", 1)[0]
    data: dict[str, str] = {}
    keys: list[str] = []
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if not match:
            errors.append(f"Unsupported frontmatter line: {line}")
            continue
        key, value = match.groups()
        keys.append(key)
        data[key] = value.strip().strip('"\'')
    if keys != ["name", "description"]:
        errors.append("SKILL.md frontmatter must contain only name and description, in that order.")
    return data, errors


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate(root: Path = ROOT, run_smoke: bool = True) -> tuple[list[str], list[str], dict[str, object]]:
    errors: list[str] = []
    warnings: list[str] = []
    details: dict[str, object] = {}

    for relative in REQUIRED:
        if not (root / relative).is_file():
            errors.append(f"Missing required file: {relative}")

    skill_path = root / "SKILL.md"
    if skill_path.is_file():
        text = skill_path.read_text(encoding="utf-8")
        metadata, metadata_errors = _frontmatter(text)
        errors.extend(metadata_errors)
        if metadata.get("name") != NAME:
            errors.append(f"SKILL.md name must be {NAME}.")
        description = metadata.get("description", "")
        if len(description) < 160 or "TODO" in description:
            errors.append("SKILL.md description must be complete and trigger-rich.")
        line_count = len(text.splitlines())
        details["skill_lines"] = line_count
        if line_count >= 500:
            errors.append("SKILL.md must stay below 500 lines; move details to references.")
        routed_paths = sorted(
            set(re.findall(r"`((?:references|assets|scripts)/[A-Za-z0-9_./-]+)`", text))
        )
        for relative in routed_paths:
            if not (root / relative).exists():
                errors.append(f"SKILL.md routes to a missing resource: {relative}")
        details["routed_resources"] = len(routed_paths)

    openai_yaml = root / "agents/openai.yaml"
    if openai_yaml.is_file():
        ui = openai_yaml.read_text(encoding="utf-8")
        if f"${NAME}" not in ui:
            errors.append("agents/openai.yaml default_prompt must mention the skill explicitly.")
        if "short_description:" not in ui or "display_name:" not in ui:
            errors.append("agents/openai.yaml is missing required interface metadata.")

    manifest_path = root / "references/project_manifest.json"
    if manifest_path.is_file():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid project manifest: {exc}")
        else:
            details["version"] = manifest.get("version")
            if manifest.get("version") != "0.4.0":
                errors.append("Project manifest version must be 0.4.0.")
            if manifest.get("status") != "expanded-partial-calibration":
                errors.append("Project manifest must use expanded-partial-calibration status.")
            if manifest.get("full_corpus_claim") is not False:
                errors.append("Project manifest must not claim full-corpus completion.")
            if manifest.get("copyrighted_full_text_included") is not False:
                errors.append("Project manifest must declare copyrighted full text excluded.")
            manifest_counts = {
                "owner_provided_fulltext_papers": 42,
                "verified_open_access_fulltext_papers": 31,
                "expanded_verified_fulltext_papers": 73,
                "deep_read_notes_completed": 73,
                "attachment_ieee_transactions_papers": 17,
                "selected_transactions_attachment_covered": 17,
                "owner_priority_transactions_rows": 17,
                "owner_priority_transactions_covered": 17,
                "owner_deprioritized_transactions_rows": 1,
            }
            for key, value in manifest_counts.items():
                if manifest.get(key) != value:
                    errors.append(f"Project manifest {key} must be {value}; found {manifest.get(key)!r}.")
            if manifest.get("sentence_style_source_status") != "attachment-key-corpus-calibrated":
                errors.append("Sentence-style metrics must retain the attachment corpus source boundary.")
            for key in (
                "local_attachment_manifest",
                "local_corpus_metrics",
                "open_access_fulltext_manifest",
                "expanded_fulltext_corpus_summary",
                "fulltext_corpus_derived_doctrine",
            ):
                relative = manifest.get(key)
                if not isinstance(relative, str) or not (root / "references" / relative).is_file():
                    errors.append(f"Project manifest path is missing or invalid for {key}: {relative!r}.")

    oa_dois: list[str] = []
    oa_titles: list[str] = []
    oa_path = root / "references/corpus/open_access_fulltext_manifest.csv"
    if oa_path.is_file():
        with oa_path.open(newline="", encoding="utf-8") as handle:
            oa_rows = list(csv.DictReader(handle))
        details["open_access_rows"] = len(oa_rows)
        oa_dois = [(row.get("doi") or "").strip().lower() for row in oa_rows]
        oa_titles = [
            re.sub(r"[^a-z0-9]+", " ", (row.get("title") or "").lower()).strip()
            for row in oa_rows
        ]
        if len(oa_rows) != 31:
            errors.append(f"Expected 31 open-access corpus rows; found {len(oa_rows)}.")
        if any(not doi for doi in oa_dois) or len(set(oa_dois)) != len(oa_dois):
            errors.append("Open-access corpus has missing or duplicate DOI values.")
        forbidden_columns = {"fulltext_url", "local_source_path", "source_filename", "extracted_text"}
        if oa_rows and forbidden_columns.intersection(oa_rows[0]):
            errors.append("Open-access manifest exposes private/download-specific columns.")
        for row in oa_rows:
            if row.get("verification_status") != "verified_for_deep_read":
                errors.append(f"Open-access row is not verified for deep read: {row.get('doi')}")
            if row.get("fulltext_format") not in {"pdf", "publisher_html"}:
                errors.append(f"Unsupported open-access full-text format: {row.get('doi')}")
            if not (row.get("landing_page_url") or "").startswith("https://"):
                errors.append(f"Open-access landing page must use HTTPS: {row.get('doi')}")

    expanded_summary_path = root / "references/corpus/expanded_fulltext_corpus_summary.json"
    if expanded_summary_path.is_file():
        try:
            expanded = json.loads(expanded_summary_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid expanded corpus summary: {exc}")
        else:
            details["expanded_corpus_status"] = expanded.get("status")
            expected_counts = {
                "owner_provided_fulltexts": 42,
                "verified_open_access_fulltexts": 31,
                "verified_fulltexts_total": 73,
                "deep_read_notes_completed": 73,
            }
            counts = expanded.get("counts", {})
            for key, value in expected_counts.items():
                if counts.get(key) != value:
                    errors.append(f"Expanded corpus summary {key} must be {value}; found {counts.get(key)!r}.")
            if expanded.get("status") != "expanded-partial-calibration":
                errors.append("Expanded corpus summary has an unsupported status.")
            if expanded.get("complete_publication_universe") is not False:
                errors.append("Expanded corpus summary must not claim a complete publication universe.")
            if expanded.get("article_fulltext_or_notes_included") is not False:
                errors.append("Expanded corpus summary must declare article full text and notes excluded.")

    corpus_path = root / "references/corpus/local_attachment_manifest.csv"
    if corpus_path.is_file():
        with corpus_path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        ids = [row.get("paper_id", "") for row in rows]
        hashes = [row.get("sha256", "") for row in rows]
        local_dois = [(row.get("doi") or "").strip().lower() for row in rows]
        local_titles = [
            re.sub(r"[^a-z0-9]+", " ", (row.get("title") or "").lower()).strip()
            for row in rows
        ]
        details["corpus_rows"] = len(rows)
        if len(rows) != 42:
            errors.append(f"Expected 42 attachment-corpus rows; found {len(rows)}.")
        if len(set(ids)) != len(ids) or any(not value for value in ids):
            errors.append("Attachment corpus has missing or duplicate paper IDs.")
        if len(set(hashes)) != len(hashes) or any(not re.fullmatch(r"[0-9a-f]{64}", value) for value in hashes):
            errors.append("Attachment corpus has missing, duplicate, or invalid SHA-256 values.")
        doi_overlap = sorted(set(local_dois).intersection(oa_dois) - {""})
        title_overlap = sorted(set(local_titles).intersection(oa_titles) - {""})
        if doi_overlap or title_overlap:
            errors.append(
                f"Local and open-access expansion are not disjoint: doi={doi_overlap}, title={title_overlap}."
            )
        for row in rows:
            signals: list[float] = []
            if row.get("author_position") == "1":
                signals.append(1.50)
            if row.get("corresponding_status") == "yes":
                signals.append(2.00)
            role = row.get("credit_role")
            if role == "original_draft":
                signals.append(2.00)
            elif role == "review_editing":
                signals.append(0.80)
            elif role == "nonwriting_contribution":
                signals.append(0.40)
            authorship_weight = max(signals or [0.45])
            try:
                year = int(row.get("year") or 0)
                tracked_weight = float(row.get("style_weight") or 0)
            except ValueError:
                errors.append(f"Invalid year or style weight for {row.get('paper_id')}.")
                continue
            recency_weight = 1.50 if year >= 2024 else 1.15 if year >= 2019 else 1.00
            venue_weight = 1.15 if row.get("is_ieee_transactions") == "yes" else 1.00
            expected_weight = round(authorship_weight * recency_weight * venue_weight, 3)
            if abs(tracked_weight - expected_weight) > 0.0005:
                errors.append(
                    f"Style weight drift for {row.get('paper_id')}: "
                    f"expected {expected_weight:.3f}, found {tracked_weight:.3f}."
                )

    publication_path = root / "references/corpus/publication_manifest.csv"
    if publication_path.is_file():
        with publication_path.open(newline="", encoding="utf-8") as handle:
            publication_rows = list(csv.DictReader(handle))
        details["selected_transactions_rows"] = len(publication_rows)
        priority_rows = [
            row for row in publication_rows
            if (row.get("style_eligible") or "").lower().startswith("yes")
        ]
        checked_priority = [
            row for row in priority_rows
            if (row.get("fulltext_status") or "").lower() == "attachment_analyzed"
        ]
        if len(publication_rows) != 18:
            errors.append(f"Expected 18 selected Transactions rows; found {len(publication_rows)}.")
        if len(priority_rows) != 17 or len(checked_priority) != 17:
            errors.append(
                "The owner-priority selected Transactions set must contain 17 rows, all attachment-analyzed."
            )
        deprioritized = [
            row for row in publication_rows
            if (row.get("style_eligible") or "").lower() == "owner_deprioritized"
        ]
        if len(deprioritized) != 1 or deprioritized[0].get("paper_id") != "2020-tifs-pca-face":
            errors.append("Exactly the 2020 PCA face-recognition row must be owner-deprioritized.")
        for row in checked_priority:
            card = row.get("paper_card") or ""
            if not card or not (root / "references" / card).is_file():
                errors.append(f"Selected Transactions row has a missing paper card: {row.get('paper_id')}")

    metrics_path = root / "references/corpus/local_corpus_metrics.json"
    if metrics_path.is_file():
        try:
            metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid local corpus metrics: {exc}")
        else:
            counts = metrics.get("counts", {})
            expected = {
                "first_author": 15,
                "corresponding_author": 9,
                "core_voice_distinct": 20,
                "ieee_transactions": 17,
                "all_ieee_venues": 20,
                "recent_2024_plus": 19,
            }
            for key, value in expected.items():
                if counts.get(key) != value:
                    errors.append(f"Corpus metric {key} must be {value}; found {counts.get(key)!r}.")
            if metrics.get("profile_status") != "attachment-key-corpus-calibrated":
                errors.append("Corpus metrics use an unsupported profile status.")
            source_boundary = metrics.get("source_boundary", {})
            boundary_expected = {
                "owner_provided_fulltext_pdfs": 42,
                "selected_transactions_with_attachment_fulltext": 17,
                "owner_priority_transactions_rows": 17,
                "owner_priority_transactions_with_fulltext": 17,
                "owner_deprioritized_transactions_rows": 1,
            }
            for key, value in boundary_expected.items():
                if source_boundary.get(key) != value:
                    errors.append(f"Corpus source boundary {key} must be {value}; found {source_boundary.get(key)!r}.")
            if counts.get("style_tiers", {}).get("C_research_architecture_only") != 19:
                errors.append("Corpus must contain 19 Tier-C research-architecture papers.")

    paper_cards = root / "references/corpus/attachment_paper_cards"
    if paper_cards.is_dir():
        card_count = len(list(paper_cards.glob("*.md")))
        details["paper_cards"] = card_count
        if card_count != 42:
            errors.append(f"Expected 42 derived paper cards; found {card_count}.")

    file_count = 0
    total_bytes = 0
    for path in root.rglob("*"):
        if path.is_symlink():
            errors.append(f"Symlinks are not allowed in the skill: {path.relative_to(root)}")
            continue
        if not path.is_file():
            continue
        file_count += 1
        total_bytes += path.stat().st_size
        relative = path.relative_to(root)
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"Forbidden release file type: {relative}")
        if any(part in FORBIDDEN_PARTS for part in relative.parts):
            errors.append(f"Private, raw, cache, or checkpoint path is not allowed: {relative}")
    details["files"] = file_count
    details["bytes"] = total_bytes

    try:
        import yaml  # type: ignore
    except ImportError:
        warnings.append("PyYAML is unavailable; deep YAML parsing was skipped.")
    else:
        yaml_files = sorted((root / "references").rglob("*.yaml")) + sorted(
            (root / "assets/templates").glob("*.yaml")
        )
        for path in yaml_files:
            try:
                yaml.safe_load(path.read_text(encoding="utf-8"))
            except Exception as exc:
                errors.append(f"Invalid YAML in {path.relative_to(root)}: {exc}")
        details["yaml_files_parsed"] = len(yaml_files)

    json_files = sorted((root / "references").rglob("*.json")) + sorted(
        (root / "assets/templates").glob("*.json")
    )
    for path in json_files:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            errors.append(f"Invalid JSON in {path.relative_to(root)}: {exc}")
    details["json_files_parsed"] = len(json_files)

    if run_smoke and not errors:
        scripts = root / "scripts"
        sys.path.insert(0, str(scripts))
        try:
            from luxing_ieee_skill.evidence import build_evidence_recommendation
            from luxing_ieee_skill.scaffold import ASSET_TEMPLATE_TARGETS, create_project
            from luxing_ieee_skill.topology import recommend_topology_design

            evidence = build_evidence_recommendation("control_performance")
            topology = recommend_topology_design("real_topology")
            with tempfile.TemporaryDirectory() as temporary:
                project = create_project("Validation Paper", "TIFS", Path(temporary) / "paper")
                scaffold_files = (
                    "PROJECT_CONFIG.yaml",
                    "evidence/EVIDENCE_PLAN.json",
                    "topology/TOPOLOGY_CARD.yaml",
                    "simulation/SYNTHETIC_SCENARIO_SPEC.yaml",
                    "planning/CROSS_PAPER_CONSISTENCY_LEDGER.csv",
                    "planning/THEOREM_TO_CODE_MAP.csv",
                    "manuscript/main.tex",
                )
                if not all((project / item).is_file() for item in scaffold_files):
                    errors.append("Bundled project scaffold is incomplete.")
                generated_dataset_card = (project / "data/DATASET_CARD.yaml").read_text(encoding="utf-8")
                canonical_dataset_card = (root / "assets/templates/DATASET_CARD.yaml").read_text(encoding="utf-8")
                if generated_dataset_card != canonical_dataset_card:
                    errors.append("Project scaffold does not consume the canonical dataset-card template.")
                for relative, canonical_name in (
                    ("planning/CROSS_PAPER_CONSISTENCY_LEDGER.csv", "CROSS_PAPER_CONSISTENCY_LEDGER.csv"),
                    ("planning/THEOREM_TO_CODE_MAP.csv", "THEOREM_TO_CODE_MAP.csv"),
                ):
                    generated = (project / relative).read_text(encoding="utf-8")
                    canonical = (root / "assets/templates" / canonical_name).read_text(encoding="utf-8")
                    if generated != canonical:
                        errors.append(f"Project scaffold does not consume canonical {canonical_name}.")
                generated_config = (project / "PROJECT_CONFIG.yaml").read_text(encoding="utf-8")
                if "project_name: Validation Paper" not in generated_config or "target_journal: TIFS" not in generated_config:
                    errors.append("Project scaffold did not render the project name and journal into the canonical config.")
            canonical_templates = {path.name for path in (root / "assets/templates").iterdir() if path.is_file()}
            if canonical_templates != set(ASSET_TEMPLATE_TARGETS):
                missing = sorted(canonical_templates - set(ASSET_TEMPLATE_TARGETS))
                stale = sorted(set(ASSET_TEMPLATE_TARGETS) - canonical_templates)
                errors.append(f"Template-to-scaffold mapping drift: unmapped={missing}, missing_assets={stale}.")
            recommended_tracks = evidence.get("recommended_tracks", [])
            if not recommended_tracks or recommended_tracks[0] not in {"A", "B", "C", "D", "E"}:
                errors.append("Evidence recommender returned an invalid primary track.")
            if topology.get("recommended_level") not in {"T1", "T2", "T3", "T4", "T5"}:
                errors.append("Topology recommender returned an invalid level.")
        except Exception as exc:  # pragma: no cover - validation surface
            errors.append(f"Runtime smoke validation failed: {exc}")
        finally:
            if sys.path and sys.path[0] == str(scripts):
                sys.path.pop(0)

    details["skill_sha256"] = _sha256(skill_path) if skill_path.is_file() else None
    return errors, warnings, details


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--no-smoke", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors, warnings, details = validate(args.root.resolve(), run_smoke=not args.no_smoke)
    payload = {"ok": not errors, "errors": errors, "warnings": warnings, "details": details}
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        for warning in warnings:
            print(f"WARNING: {warning}")
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"Validation {'passed' if not errors else 'failed'}: {args.root.resolve()}")
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
