"""Command-line interface."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .corpus import (
    build_queue,
    coverage_summary,
    load_manifest,
    make_deakin_proxy_url,
    validate_manifest,
    verify_local_attachment_corpus,
    write_queue,
)
from .evidence import audit_evidence_plan, build_evidence_recommendation, load_evidence_plan, render_evidence_report
from .linter import lint_text, render_markdown_report
from .local_corpus import analyze_private_attachment_corpus, write_private_corpus_audit
from .metrics import aggregate_metrics, analyze_text
from .scaffold import create_project
from .textio import iter_documents, read_text
from .topology import (
    audit_topology_card,
    load_topology_card,
    recommend_topology_design,
    render_topology_report,
)


def _repo_root() -> Path:
    candidate = Path(__file__).resolve()
    for parent in candidate.parents:
        if (parent / "SKILL.md").exists() and (parent / "references/project_manifest.json").exists():
            return parent
    return Path.cwd()


def command_analyze(args: argparse.Namespace) -> int:
    documents = []
    results = []
    for path in iter_documents(args.path, recursive=not args.no_recursive):
        try:
            text = read_text(path)
        except RuntimeError as exc:
            print(f"SKIP {path}: {exc}", file=sys.stderr)
            continue
        metrics = analyze_text(text, source=str(path))
        results.append(metrics)
        weight = 1.0
        documents.append((metrics, weight))
    payload = {"documents": results, "aggregate": aggregate_metrics(documents)}
    rendered = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
        print(output)
    else:
        print(rendered)
    return 0 if results else 2


def command_check(args: argparse.Namespace) -> int:
    text = read_text(args.path)
    issues = lint_text(text, source=str(args.path))
    report = render_markdown_report(issues, source=str(args.path))
    if args.report:
        output = Path(args.report)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
        print(output)
    else:
        print(report)
    major = sum(issue.severity in {"blocking", "major"} for issue in issues)
    return 1 if major and args.fail_on_major else 0


def command_queue(args: argparse.Namespace) -> int:
    records = load_manifest(args.manifest)
    errors = validate_manifest(records)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 2
    rows = build_queue(records, include_checked=args.include_checked)
    write_queue(args.output, rows)
    print(json.dumps({"queue": str(args.output), "rows": len(rows), "coverage": coverage_summary(records)}, indent=2))
    return 0


def command_proxy(args: argparse.Namespace) -> int:
    print(make_deakin_proxy_url(args.url))
    return 0


def command_new_project(args: argparse.Namespace) -> int:
    path = create_project(args.name, args.journal.upper(), args.output, force=args.force)
    print(path)
    return 0



def command_recommend_evidence(args: argparse.Namespace) -> int:
    payload = build_evidence_recommendation(args.claim_type)
    print(json.dumps(payload, indent=2))
    return 0 if not payload["manual_review_required"] else 2


def command_audit_evidence(args: argparse.Namespace) -> int:
    plan = load_evidence_plan(args.path)
    issues = audit_evidence_plan(plan)
    report = render_evidence_report(issues, plan, source=str(args.path))
    if args.report:
        output = Path(args.report)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
        print(output)
    else:
        print(report)
    blocking = any(issue.severity == "blocking" for issue in issues)
    major = any(issue.severity == "major" for issue in issues)
    return 1 if blocking or (major and args.fail_on_major) else 0


def command_verify_local_corpus(args: argparse.Namespace) -> int:
    root = _repo_root()
    manifest = Path(args.manifest) if args.manifest else root / "references/corpus/local_attachment_manifest.csv"
    payload = verify_local_attachment_corpus(args.directory, manifest)
    rendered = json.dumps(payload, indent=2, ensure_ascii=False)
    if args.report:
        output = Path(args.report)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered + "\n", encoding="utf-8")
        print(output)
    else:
        print(rendered)
    return 0 if payload["complete_exact_match"] else 1


def command_analyze_local_corpus(args: argparse.Namespace) -> int:
    root = _repo_root()
    manifest = Path(args.manifest) if args.manifest else root / "references/corpus/local_attachment_manifest.csv"
    payload = analyze_private_attachment_corpus(
        args.directory,
        manifest,
        max_word_delta=args.max_word_delta,
        max_sentence_delta=args.max_sentence_delta,
    )
    if args.report:
        output = write_private_corpus_audit(args.report, payload)
        print(output)
    else:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    if not payload["analysis_complete"]:
        return 1
    if args.fail_on_drift and not payload["tracked_metric_reproduction_within_tolerance"]:
        return 1
    return 0


def command_recommend_topology(args: argparse.Namespace) -> int:
    payload = recommend_topology_design(args.availability)
    print(json.dumps(payload, indent=2, ensure_ascii=False))
    return 0 if not payload["manual_review_required"] else 2


def command_audit_topology(args: argparse.Namespace) -> int:
    card = load_topology_card(args.path)
    issues = audit_topology_card(card)
    report = render_topology_report(issues, card, source=str(args.path))
    if args.report:
        output = Path(args.report)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(report, encoding="utf-8")
        print(output)
    else:
        print(report)
    blocking = any(issue.severity == "blocking" for issue in issues)
    major = any(issue.severity == "major" for issue in issues)
    return 1 if blocking or (major and args.fail_on_major) else 0


def command_validate(args: argparse.Namespace) -> int:
    root = Path(args.root) if args.root else _repo_root()
    sys.path.insert(0, str(root / "scripts"))
    try:
        from validate_skill import validate  # type: ignore
    except ImportError as exc:
        print(f"Could not import skill validator from {root / 'scripts'}: {exc}", file=sys.stderr)
        return 2
    errors, warnings, _ = validate(root, run_smoke=False)
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"Validation passed: {root}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="luxing-ieee-skill")
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze = subparsers.add_parser("analyze", help="Compute prose metrics for a file or directory.")
    analyze.add_argument("path")
    analyze.add_argument("--output")
    analyze.add_argument("--no-recursive", action="store_true")
    analyze.set_defaults(func=command_analyze)

    check = subparsers.add_parser("check", help="Run deterministic manuscript preflight checks.")
    check.add_argument("path")
    check.add_argument("--report")
    check.add_argument("--fail-on-major", action="store_true")
    check.set_defaults(func=command_check)

    queue = subparsers.add_parser("queue", help="Build a Deakin-safe full-text audit queue.")
    queue.add_argument(
        "--manifest",
        default=str(_repo_root() / "references/corpus/publication_manifest.csv"),
    )
    queue.add_argument("--output", default="reports/fulltext_queue.csv")
    queue.add_argument("--include-checked", action="store_true")
    queue.set_defaults(func=command_queue)

    proxy = subparsers.add_parser("proxy", help="Generate a Deakin EZproxy URL.")
    proxy.add_argument("url")
    proxy.set_defaults(func=command_proxy)

    new_project = subparsers.add_parser("new-project", help="Create a research project scaffold.")
    new_project.add_argument("--name", required=True)
    new_project.add_argument("--journal", default="TIFS")
    new_project.add_argument("--output", required=True)
    new_project.add_argument("--force", action="store_true")
    new_project.set_defaults(func=command_new_project)

    recommend_evidence = subparsers.add_parser(
        "recommend-evidence", help="Recommend evidence tracks and repository layers for a claim type."
    )
    recommend_evidence.add_argument(
        "--claim-type",
        required=True,
        choices=[
            "mechanism",
            "numerical_method",
            "control_performance",
            "game_stability",
            "parameter_recovery",
            "predictive_generalization",
            "operational_feasibility",
            "causal_effect",
        ],
    )
    recommend_evidence.set_defaults(func=command_recommend_evidence)

    audit_evidence = subparsers.add_parser(
        "audit-evidence", help="Audit a numerical, simulation, real-data, or testbed evidence plan."
    )
    audit_evidence.add_argument("path")
    audit_evidence.add_argument("--report")
    audit_evidence.add_argument("--fail-on-major", action="store_true")
    audit_evidence.set_defaults(func=command_audit_evidence)

    verify_local = subparsers.add_parser(
        "verify-local-corpus",
        help="Verify owner-provided private PDFs against the tracked attachment checksum manifest.",
    )
    verify_local.add_argument("directory")
    verify_local.add_argument("--manifest")
    verify_local.add_argument("--report")
    verify_local.set_defaults(func=command_verify_local_corpus)

    analyze_local = subparsers.add_parser(
        "analyze-local-corpus",
        help="Recompute derived-only metrics for the private owner-provided PDF corpus without OCR.",
    )
    analyze_local.add_argument("directory")
    analyze_local.add_argument("--manifest")
    analyze_local.add_argument("--report")
    analyze_local.add_argument("--max-word-delta", type=int, default=40)
    analyze_local.add_argument("--max-sentence-delta", type=int, default=5)
    analyze_local.add_argument("--fail-on-drift", action="store_true")
    analyze_local.set_defaults(func=command_analyze_local_corpus)

    recommend_topology = subparsers.add_parser(
        "recommend-topology",
        help="Recommend the highest defensible topology evidence level from available sources.",
    )
    recommend_topology.add_argument(
        "--availability",
        required=True,
        choices=["real_outcomes", "temporal_trace", "real_topology", "topology_statistics", "none"],
    )
    recommend_topology.set_defaults(func=command_recommend_topology)

    audit_topology = subparsers.add_parser(
        "audit-topology",
        help="Audit a node-level topology card and topology/simulation claim boundary.",
    )
    audit_topology.add_argument("path")
    audit_topology.add_argument("--report")
    audit_topology.add_argument("--fail-on-major", action="store_true")
    audit_topology.set_defaults(func=command_audit_topology)

    validate = subparsers.add_parser("validate", help="Validate this skill repository.")
    validate.add_argument("--root")
    validate.set_defaults(func=command_validate)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return int(args.func(args))
