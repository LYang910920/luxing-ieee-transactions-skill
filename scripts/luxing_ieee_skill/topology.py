"""Topology-first evidence planning and deterministic graph-card audits."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any


TOPOLOGY_LEVELS = {
    "T1": "observed real topology with declared synthetic or assumed dynamics",
    "T2": "observed topology plus empirical node/edge attributes, with calibrated and assumed quantities separated",
    "T3": "temporal/contact topology or timestamped trace with counterfactual interventions",
    "T4": "synthetic topology fitted or matched to observed graph statistics",
    "T5": "fully controlled synthetic topology and dynamics",
}

AVAILABILITY_LEVELS = {
    "real_outcomes": ["D_or_E", "Observed outcomes may support calibration, prediction, operational, or causal designs; topology remains separately documented."],
    "temporal_trace": ["T3", TOPOLOGY_LEVELS["T3"]],
    "real_topology": ["T1", TOPOLOGY_LEVELS["T1"]],
    "topology_statistics": ["T4", TOPOLOGY_LEVELS["T4"]],
    "none": ["T5", TOPOLOGY_LEVELS["T5"]],
}

COMMON_GENERATOR_FAMILIES = [
    "erdos_renyi",
    "barabasi_albert_or_scale_free",
    "watts_strogatz",
    "stochastic_block_model",
    "configuration_model",
]


@dataclass(frozen=True)
class TopologyIssue:
    severity: str
    code: str
    message: str


def _missing(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip() or value.strip().upper() in {
            "TBD",
            "TODO",
            "UNKNOWN",
            "NONE",
        }
    if isinstance(value, (list, tuple, dict, set)):
        return len(value) == 0
    return False


def _dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _bool(value: Any) -> bool:
    return value is True


def load_topology_card(path: str | Path) -> dict[str, Any]:
    """Load a JSON-compatible YAML topology card.

    The shipped ``.yaml`` template is intentionally JSON syntax, which is valid
    YAML 1.2 and keeps the core package dependency-free.
    """

    card_path = Path(path)
    try:
        payload = json.loads(card_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Topology card must use the shipped JSON-compatible YAML syntax: {card_path}: {exc}"
        ) from exc
    if not isinstance(payload, dict):
        raise ValueError(f"Topology card must contain an object: {card_path}")
    return payload


def recommend_topology_design(availability: str) -> dict[str, Any]:
    """Recommend the highest defensible topology evidence level."""

    key = availability.strip().lower()
    level, label = AVAILABILITY_LEVELS.get(key, ["manual_review", "Unknown availability category."])
    minimum = {
        "T1": [
            "official topology source, terms, version/hash, and topology card",
            "explicit declaration that dynamics/parameters/interventions are simulated when applicable",
            "matched synthetic graph controls",
            "multiple graph, parameter, and attack-seed scenarios",
            "independent solver or stochastic-ensemble validation",
        ],
        "T2": [
            "all T1 requirements",
            "provenance and uncertainty for every empirical node/edge attribute",
            "separation of observed, calibrated, assumed, and synthetic quantities",
        ],
        "T3": [
            "timestamp/entity mapping and event ordering",
            "future-label leakage prevention",
            "recorded exogenous events separated from counterfactual interventions",
            "complete temporal/scenario holdouts",
            "fidelity and response-assumption boundary",
        ],
        "T4": [
            "official target graph statistics and source",
            "declared graph generator/fitting method",
            "goodness-of-match table",
            "multiple generated graph instances",
            "sensitivity to unmatched statistics",
        ],
        "T5": [
            "at least two graph families for topology-sensitive claims",
            "multiple sizes, graph seeds, parameter seeds, and attack-seed rules",
            "independent numerical or stochastic validation",
            "matched baselines and uncertainty",
            "model-conditional claim language",
        ],
    }.get(level, [])
    return {
        "availability": key,
        "recommended_level": level,
        "description": label,
        "minimum_requirements": minimum,
        "claim_boundary": (
            "Observed topology does not make dynamics, parameters, interventions, or outcomes observed. "
            "Synthetic evidence remains conditional on the declared model and scenario design."
        ),
        "manual_review_required": level == "manual_review",
    }


def audit_topology_card(card: dict[str, Any]) -> list[TopologyIssue]:
    """Audit a topology card without changing it."""

    issues: list[TopologyIssue] = []

    def add(severity: str, code: str, message: str) -> None:
        issues.append(TopologyIssue(severity, code, message))

    level = str(card.get("topology_evidence_level", "")).strip().upper()
    source_type = str(card.get("source_type", "")).strip().lower()
    graph = _dict(card.get("graph"))
    prep = _dict(card.get("preprocessing"))
    synth = _dict(card.get("synthetic_design"))
    split = _dict(card.get("split"))
    mapping = _dict(card.get("model_mapping"))
    validation = _dict(card.get("validation"))

    if _missing(card.get("topology_id")):
        add("blocking", "TOPOLOGY_ID_MISSING", "Assign a stable topology identifier.")
    if level not in TOPOLOGY_LEVELS:
        add("blocking", "TOPOLOGY_LEVEL_INVALID", "Use topology evidence level T1, T2, T3, T4, or T5.")
    if _missing(card.get("scientific_role")):
        add("blocking", "GRAPH_ROLE_MISSING", "Define whether edges represent contact, communication, influence, dependency, attack paths, or another mechanism.")
    if _missing(source_type):
        add("blocking", "GRAPH_SOURCE_TYPE_MISSING", "Classify the source as observed, temporal_observed, statistic_matched, or synthetic.")

    for field, code, msg in (
        ("node_unit", "NODE_UNIT_MISSING", "Define the scientific meaning/unit of a node."),
        ("edge_unit", "EDGE_UNIT_MISSING", "Define the scientific meaning/unit of an edge."),
        ("adjacency_semantics", "ADJACENCY_SEMANTICS_MISSING", "State exactly what A[i,j] means."),
        ("self_loop_policy", "SELF_LOOP_POLICY_MISSING", "State how self-loops are handled."),
        ("parallel_edge_policy", "PARALLEL_EDGE_POLICY_MISSING", "State how duplicate/parallel edges are handled."),
        ("isolated_node_policy", "ISOLATE_POLICY_MISSING", "State how isolated nodes are handled."),
        ("component_policy", "COMPONENT_POLICY_MISSING", "State whether all components, the largest component, or a justified subset is used."),
        ("normalization", "NORMALIZATION_MISSING", "State the adjacency/weight normalization."),
    ):
        if _missing(graph.get(field)):
            add("blocking", code, msg)

    observed_level = level in {"T1", "T2", "T3"}
    if observed_level:
        for field, code, msg in (
            ("source_name", "OBSERVED_SOURCE_MISSING", "Record the official topology/trace source."),
            ("official_url", "OBSERVED_SOURCE_URL_MISSING", "Record the official source URL."),
            ("licence_or_terms", "GRAPH_TERMS_MISSING", "Record licence or data-use terms."),
            ("version_or_hash", "GRAPH_VERSION_MISSING", "Record a version, date, or checksum."),
        ):
            if _missing(card.get(field)):
                add("blocking", code, msg)
        if not _bool(card.get("license_checked")):
            add("blocking", "GRAPH_LICENSE_UNCHECKED", "Review topology licence/data-use terms.")
        if not _bool(card.get("version_or_hash_recorded")):
            add("blocking", "GRAPH_VERSION_UNRECORDED", "Record a source version or checksum.")
        if _missing(prep.get("script")):
            add("blocking", "GRAPH_PREPROCESSING_SCRIPT_MISSING", "Use a deterministic graph preprocessing script.")
        if not _bool(prep.get("deterministic")):
            add("major", "GRAPH_PREPROCESSING_NOT_DETERMINISTIC", "Make preprocessing deterministic or record every random seed.")
        if not _bool(prep.get("raw_immutable_copy")):
            add("major", "GRAPH_RAW_COPY_NOT_IMMUTABLE", "Keep an immutable raw copy outside Git.")
        if _missing(prep.get("statistics_before")) or _missing(prep.get("statistics_after")):
            add("blocking", "GRAPH_STATISTICS_MISSING", "Record graph statistics before and after preprocessing.")
        if _missing(prep.get("validation_checks")):
            add("major", "GRAPH_PREPROCESSING_VALIDATION_MISSING", "Add node/edge count, direction, weight, identifier, and checksum checks.")

    if level == "T3":
        if graph.get("temporal") is not True:
            add("blocking", "TEMPORAL_GRAPH_FLAG_MISSING", "T3 requires a temporal topology or timestamped trace.")
        if _missing(graph.get("timestamp_handling")) or str(graph.get("timestamp_handling", "")).lower() == "not_applicable":
            add("blocking", "TIMESTAMP_HANDLING_MISSING", "Define timestamp ordering, windowing, ties, and timezone/clock handling.")

    seeds = synth.get("graph_seeds")
    try:
        seed_count = len(seeds) if isinstance(seeds, list) else 0
    except TypeError:
        seed_count = 0

    if level == "T4":
        if _missing(synth.get("generator_families")):
            add("blocking", "SYNTHETIC_GENERATOR_MISSING", "T4 requires a declared graph generator.")
        if _missing(synth.get("target_observed_statistics")):
            add("blocking", "TARGET_GRAPH_STATISTICS_MISSING", "List the observed statistics being matched.")
        if _missing(synth.get("goodness_of_match")) or str(synth.get("goodness_of_match", "")).lower() == "not_applicable":
            add("blocking", "GRAPH_GOODNESS_OF_MATCH_MISSING", "Define and report graph-statistic goodness of match.")
        if seed_count < 3:
            add("major", "GRAPH_INSTANCE_COUNT_LOW", "Use at least three generated graph instances unless a stronger justification is documented.")

    if level == "T5":
        families = synth.get("generator_families")
        family_count = len(families) if isinstance(families, list) else 0
        if family_count < 2:
            add("major", "SYNTHETIC_GRAPH_FAMILIES_LOW", "Topology-sensitive claims normally require at least two graph families.")
        if seed_count < 3:
            add("major", "GRAPH_INSTANCE_COUNT_LOW", "Use at least three graph seeds/instances.")
        if source_type not in {"synthetic", "statistic_matched"}:
            add("major", "SOURCE_LEVEL_MISMATCH", "T5 should normally be classified as a synthetic source.")

    if _missing(mapping.get("graph_to_model_map")):
        add("blocking", "GRAPH_MODEL_MAP_MISSING", "Map raw node/edge fields to the model adjacency, states, and attributes.")
    if _missing(mapping.get("dynamics_observed_or_synthetic")):
        add("blocking", "DYNAMICS_REALITY_MISSING", "Classify dynamics as observed, calibrated, synthetic, or mixed.")
    if _missing(mapping.get("parameter_provenance")):
        add("blocking", "PARAMETER_PROVENANCE_MISSING", "Record whether model parameters are observed, calibrated, assumed, or generated.")
    if _missing(mapping.get("attack_seed_rules")):
        add("major", "ATTACK_SEED_RULES_MISSING", "Evaluate more than one defensible initial/attack-seed placement rule.")

    if _missing(validation.get("matched_topology_controls")):
        add("major", "MATCHED_TOPOLOGY_CONTROLS_MISSING", "Add structurally matched graph controls or explain why they are not needed.")
    if not _bool(validation.get("independent_solver_or_stochastic_ensemble")):
        add("blocking", "NODE_MODEL_INDEPENDENT_CHECK_MISSING", "Validate the node-level model with an independent solver, representation, or stochastic ensemble.")
    if not _bool(validation.get("multiple_graph_instances")):
        add("major", "MULTIPLE_GRAPH_INSTANCES_MISSING", "Evaluate more than one graph instance/snapshot when making comparative claims.")
    if not _bool(validation.get("failure_cases_retained")):
        add("major", "GRAPH_FAILURES_NOT_RETAINED", "Retain failed, divergent, or unfavorable graph/scenario runs.")

    if _bool(split.get("claims_topology_generalization")):
        if _missing(split.get("held_out_graphs_or_snapshots")):
            add("blocking", "HELD_OUT_GRAPH_MISSING", "Topology-generalization claims require held-out complete graphs or snapshots.")
        if not _bool(split.get("leakage_audit")):
            add("blocking", "GRAPH_LEAKAGE_UNCHECKED", "Audit graph, node, time, and preprocessing leakage.")

    claim_boundary = str(card.get("claim_boundary", "")).strip()
    if _missing(claim_boundary):
        add("blocking", "TOPOLOGY_CLAIM_BOUNDARY_MISSING", "State exactly what is observed, synthetic, calibrated, and counterfactual.")
    else:
        lower = claim_boundary.lower()
        if level in {"T1", "T2", "T3", "T4", "T5"} and "real-world validation" in lower:
            add("blocking", "REAL_WORLD_TOPOLOGY_OVERCLAIM", "Topology or trace use alone is not real-world validation.")
        if level in {"T4", "T5"} and ("real network" in lower or "real-world" in lower):
            add("major", "SYNTHETIC_TOPOLOGY_OVERCLAIM", "Synthetic topology must not be described as an observed real network.")
        dynamics = str(mapping.get("dynamics_observed_or_synthetic", "")).lower()
        if observed_level and dynamics in {"synthetic", "mixed", "calibrated"} and "real-topology" not in lower and "temporal" not in lower and "trace-driven" not in lower:
            add(
                "minor",
                "REAL_TOPOLOGY_LABEL_RECOMMENDED",
                "Use an explicit real-topology/temporal/trace-driven label when topology is observed but dynamics are not fully observed.",
            )

    order = {"blocking": 0, "major": 1, "minor": 2}
    return sorted(issues, key=lambda issue: (order[issue.severity], issue.code))


def render_topology_report(
    issues: list[TopologyIssue], card: dict[str, Any], source: str = ""
) -> str:
    """Render a topology audit report."""

    level = str(card.get("topology_evidence_level", "")).upper()
    counts = {
        severity: sum(issue.severity == severity for issue in issues)
        for severity in ("blocking", "major", "minor")
    }
    lines = ["# Topology Plan Audit", ""]
    if source:
        lines.extend([f"Source: `{source}`", ""])
    lines.extend(
        [
            f"- Evidence level: `{level or 'missing'}` — {TOPOLOGY_LEVELS.get(level, 'unknown')}",
            f"- Findings: {counts['blocking']} blocking, {counts['major']} major, {counts['minor']} minor",
            "",
        ]
    )
    if not issues:
        lines.extend(["## Decision", "", "PASS WITH NO AUTOMATED FLAGS", ""])
        return "\n".join(lines)
    for severity in ("blocking", "major", "minor"):
        subset = [issue for issue in issues if issue.severity == severity]
        if not subset:
            continue
        lines.extend([f"## {severity.title()}", ""])
        lines.extend(f"- **{issue.code}** — {issue.message}" for issue in subset)
        lines.append("")
    lines.extend(
        [
            "## Decision",
            "",
            "BLOCK until all blocking findings are resolved."
            if counts["blocking"]
            else "REVISE major findings before freezing node-level claims.",
            "",
        ]
    )
    return "\n".join(lines)
