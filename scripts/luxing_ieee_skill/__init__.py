"""Utilities for the Lu-Xing Yang IEEE Transactions research-and-writing skill."""

from .evidence import (
    EvidenceIssue,
    audit_evidence_plan,
    build_evidence_recommendation,
    recommend_evidence_tracks,
    recommend_repository_layers,
    render_evidence_report,
)
from .linter import Issue, lint_text, render_markdown_report
from .local_corpus import analyze_private_attachment_corpus, extract_abstract
from .topology import (
    TopologyIssue,
    audit_topology_card,
    recommend_topology_design,
    render_topology_report,
)
from .metrics import analyze_text, aggregate_metrics, segment_sections

__all__ = [
    "EvidenceIssue",
    "Issue",
    "TopologyIssue",
    "audit_evidence_plan",
    "audit_topology_card",
    "build_evidence_recommendation",
    "aggregate_metrics",
    "analyze_text",
    "analyze_private_attachment_corpus",
    "extract_abstract",
    "lint_text",
    "recommend_evidence_tracks",
    "recommend_repository_layers",
    "recommend_topology_design",
    "render_evidence_report",
    "render_topology_report",
    "render_markdown_report",
    "segment_sections",
]

__version__ = "0.4.0"
