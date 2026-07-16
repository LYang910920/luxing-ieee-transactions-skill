"""Deterministic audits for numerical, simulation, and real-data evidence plans."""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
from typing import Any

TRACKS = {
    "A": "mechanistic numerical evidence",
    "B": "stochastic, agent-based, or closed-loop simulation",
    "C": "real-topology or trace-driven semi-empirical simulation",
    "D": "real-data calibration and predictive validation",
    "E": "emulation, cyber range, hardware-in-the-loop, or field evidence",
}

CLAIM_TYPES = {
    "mechanism",
    "numerical_method",
    "control_performance",
    "game_stability",
    "parameter_recovery",
    "predictive_generalization",
    "operational_feasibility",
    "causal_effect",
}

REPOSITORY_LAYERS = {"foundation", "game_learning", "physics_informed"}

SIMULATOR_TYPES = {
    "deterministic_ode",
    "stochastic_process",
    "agent_based",
    "discrete_event",
    "sampled_closed_loop",
    "trace_replay",
    "emulation",
    "cyber_range",
    "hardware_in_loop",
}

STOCHASTIC_OR_REPEATED_TYPES = SIMULATOR_TYPES - {"deterministic_ode"}
PERFORMANCE_CLAIMS = {
    "numerical_method",
    "control_performance",
    "game_stability",
    "parameter_recovery",
    "predictive_generalization",
    "operational_feasibility",
}


@dataclass(frozen=True)
class EvidenceIssue:
    severity: str
    code: str
    message: str


def _missing(value: Any) -> bool:
    if value is None:
        return True
    if isinstance(value, str):
        return not value.strip() or value.strip().upper() in {"TBD", "TODO", "UNKNOWN", "NONE"}
    if isinstance(value, (list, tuple, dict, set)):
        return len(value) == 0
    return False


def _dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _bool(value: Any) -> bool:
    return value is True


def load_evidence_plan(path: str | Path) -> dict[str, Any]:
    """Load a JSON evidence plan and require an object at the top level."""

    plan_path = Path(path)
    try:
        payload = json.loads(plan_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON evidence plan {plan_path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise ValueError(f"Evidence plan must be a JSON object: {plan_path}")
    return payload


def recommend_evidence_tracks(main_claim_type: str) -> list[str]:
    """Return a conservative minimum/extension recommendation for one claim type."""

    mapping = {
        "mechanism": ["A", "C"],
        "numerical_method": ["A", "B"],
        "control_performance": ["B", "A", "C"],
        "game_stability": ["B", "A"],
        "parameter_recovery": ["D", "A"],
        "predictive_generalization": ["D", "C"],
        "operational_feasibility": ["E", "B"],
        "causal_effect": ["E"],
    }
    return mapping.get(main_claim_type, [])


def recommend_repository_layers(
    main_claim_type: str, primary_track: str | None = None
) -> list[str]:
    """Recommend the smallest teaching-repository layer set for a claim/track."""

    track = (primary_track or "").strip().upper()
    by_track = {
        "A": ["foundation"],
        "B": ["foundation", "game_learning"],
        "C": ["foundation", "game_learning"],
        "D": ["foundation", "physics_informed"],
        "E": ["foundation", "game_learning"],
    }
    layers = list(by_track.get(track, []))
    if main_claim_type in {"game_stability", "control_performance", "operational_feasibility"}:
        if "game_learning" not in layers:
            layers.append("game_learning")
    if main_claim_type in {"parameter_recovery", "predictive_generalization"}:
        if "physics_informed" not in layers:
            layers.append("physics_informed")
    if main_claim_type in CLAIM_TYPES and "foundation" not in layers:
        layers.insert(0, "foundation")
    return layers


def build_evidence_recommendation(main_claim_type: str) -> dict[str, Any]:
    """Return a compact claim-to-track-to-layer recommendation for planning tools."""

    tracks = recommend_evidence_tracks(main_claim_type)
    primary = tracks[0] if tracks else ""
    return {
        "main_claim_type": main_claim_type,
        "recommended_tracks": tracks,
        "recommended_repository_layers": recommend_repository_layers(main_claim_type, primary),
        "manual_review_required": not bool(tracks),
    }


def audit_evidence_plan(plan: dict[str, Any]) -> list[EvidenceIssue]:
    """Audit an evidence plan without silently rewriting it."""

    issues: list[EvidenceIssue] = []

    def add(severity: str, code: str, message: str) -> None:
        issues.append(EvidenceIssue(severity, code, message))

    project_name = plan.get("project_name")
    claim_type = str(plan.get("main_claim_type", "")).strip()
    claim_statement = plan.get("main_claim_statement")
    primary_track = str(plan.get("primary_evidence_track", "")).strip().upper()
    secondary_tracks = [str(item).strip().upper() for item in plan.get("secondary_evidence_tracks", [])]
    layers = {str(item).strip() for item in plan.get("repository_layers", [])}
    data = _dict(plan.get("data"))
    simulation = _dict(plan.get("simulation"))
    validation = _dict(plan.get("validation"))

    if _missing(project_name):
        add("blocking", "PROJECT_NAME_MISSING", "Name the project in the evidence plan.")
    if claim_type not in CLAIM_TYPES:
        add(
            "blocking",
            "CLAIM_TYPE_INVALID",
            "main_claim_type must be one of: " + ", ".join(sorted(CLAIM_TYPES)),
        )
    if _missing(claim_statement):
        add("blocking", "CLAIM_STATEMENT_MISSING", "Write the exact evidence-bearing main claim.")
    if primary_track not in TRACKS:
        add("blocking", "PRIMARY_TRACK_INVALID", "primary_evidence_track must be A, B, C, D, or E.")
    invalid_secondary = sorted(set(secondary_tracks) - set(TRACKS))
    if invalid_secondary:
        add("major", "SECONDARY_TRACK_INVALID", f"Unknown secondary tracks: {invalid_secondary}.")
    if primary_track in secondary_tracks:
        add("minor", "TRACK_DUPLICATED", "The primary evidence track is repeated as a secondary track.")

    if not layers:
        add("major", "REPOSITORY_LAYER_MISSING", "Select at least one teaching-repository layer.")
    invalid_layers = sorted(layers - REPOSITORY_LAYERS)
    if invalid_layers:
        add("major", "REPOSITORY_LAYER_INVALID", f"Unknown repository layers: {invalid_layers}.")
    if primary_track == "A" and "foundation" not in layers:
        add("major", "FOUNDATION_LAYER_EXPECTED", "Track A normally requires the Foundation layer.")
    if primary_track == "B" and "game_learning" not in layers:
        add("major", "GAME_LAYER_EXPECTED", "Track B normally requires the Game learning layer.")
    if primary_track == "D" and "physics_informed" not in layers:
        add("major", "PHYSICS_LAYER_EXPECTED", "Track D normally requires the Physics-informed layer.")

    uses_real_topology = _bool(data.get("uses_real_topology"))
    uses_real_traces = _bool(data.get("uses_real_traces"))
    uses_real_data = _bool(data.get("uses_real_data"))
    any_real_source = uses_real_topology or uses_real_traces or uses_real_data
    topology_level = str(data.get("topology_evidence_level", "")).strip().upper()
    topology_cards = data.get("topology_cards")

    if uses_real_topology:
        if topology_level not in {"T1", "T2", "T3"}:
            add(
                "blocking",
                "REAL_TOPOLOGY_LEVEL_INVALID",
                "Observed topology must be classified as T1, T2, or T3.",
            )
        if _missing(topology_cards):
            add(
                "blocking",
                "TOPOLOGY_CARD_MISSING",
                "List a topology card for every observed or generated graph source.",
            )
    elif topology_level in {"T1", "T2", "T3"}:
        add(
            "major",
            "TOPOLOGY_LEVEL_SOURCE_MISMATCH",
            "T1–T3 imply an observed topology/trace; set uses_real_topology/uses_real_traces or choose T4/T5.",
        )

    if primary_track == "C" and not any_real_source:
        add(
            "blocking",
            "SEMI_EMPIRICAL_SOURCE_MISSING",
            "Track C requires a declared real topology, trace, or other real data source.",
        )
    if primary_track == "D" and not uses_real_data:
        add("blocking", "REAL_DATA_REQUIRED", "Track D requires uses_real_data=true.")
    if primary_track == "E" and not uses_real_data:
        add(
            "major",
            "TESTBED_DATA_EXPECTED",
            "Track E should record measured testbed, emulation, hardware, or field data.",
        )

    if any_real_source:
        if _missing(data.get("dataset_cards")):
            add("blocking", "DATASET_CARD_MISSING", "List at least one dataset card for every real source.")
        if not _bool(data.get("license_checked")):
            add("blocking", "DATA_LICENSE_UNCHECKED", "Check data licence/terms and citation requirements.")
        if not _bool(data.get("version_or_hash_recorded")):
            add("major", "DATA_VERSION_UNRECORDED", "Record dataset version, DOI, snapshot, or checksum.")
        if not _bool(data.get("privacy_ethics_checked")):
            add("blocking", "DATA_ETHICS_UNCHECKED", "Complete privacy, sensitive-data, and ethics review.")
        if _missing(data.get("data_to_model_map")):
            add("blocking", "DATA_MODEL_MAP_MISSING", "Create a field/event-to-model mapping.")
        if _missing(data.get("reality_ledger")):
            add(
                "blocking",
                "REALITY_LEDGER_MISSING",
                "Separate observed, inferred, assumed, simulated, and counterfactual quantities.",
            )
        if _missing(data.get("adapter_contracts")):
            add(
                "major",
                "DATA_ADAPTER_CONTRACT_MISSING",
                "Record the parser/adapter contract that turns raw data into model inputs.",
            )
        if _missing(data.get("split_strategy")):
            add("blocking", "DATA_SPLIT_MISSING", "Declare temporal/node/host/graph/scenario splits.")
        if not _bool(data.get("leakage_audit")):
            add("blocking", "DATA_LEAKAGE_UNCHECKED", "Audit future, node, host, scenario, and preprocessing leakage.")

    uses_simulation = _bool(simulation.get("uses_simulation"))
    simulator_type = str(simulation.get("simulator_type", "")).strip()
    if primary_track in {"B", "C", "E"} and not uses_simulation:
        add("blocking", "SIMULATION_REQUIRED", f"Track {primary_track} requires a simulator/emulator contract.")
    if uses_simulation:
        if simulator_type not in SIMULATOR_TYPES:
            add(
                "blocking",
                "SIMULATOR_TYPE_INVALID",
                "simulator_type must be one of: " + ", ".join(sorted(SIMULATOR_TYPES)),
            )
        if not _bool(simulation.get("state_action_timing_defined")):
            add("blocking", "SIMULATION_TIMING_MISSING", "Define observation, action, flow/event, and reset order.")
        if _missing(simulation.get("verification_checks")):
            add("blocking", "SIMULATION_VERIFICATION_MISSING", "List equation, invariant, event, or parser checks.")
        if _missing(simulation.get("validation_target")):
            add("major", "SIMULATION_VALIDATION_TARGET_MISSING", "State what real or benchmark behavior the simulator must reproduce.")
        if _missing(simulation.get("fidelity_boundary")):
            add("blocking", "SIMULATION_FIDELITY_BOUNDARY_MISSING", "State what the simulator does and does not represent.")
        if _missing(simulation.get("synthetic_scenario_spec")):
            add(
                "major",
                "SYNTHETIC_SCENARIO_SPEC_MISSING",
                "Record graph, parameter, initial/attack-seed, decision, and replication generation in a scenario specification.",
            )
        if uses_real_traces and _missing(simulation.get("counterfactual_assumptions")):
            add(
                "blocking",
                "TRACE_COUNTERFACTUAL_ASSUMPTIONS_MISSING",
                "State how replayed exogenous events are combined with unobserved counterfactual actions.",
            )
        replications = simulation.get("replications", 0)
        try:
            replications_int = int(replications)
        except (TypeError, ValueError):
            replications_int = 0
        if simulator_type in STOCHASTIC_OR_REPEATED_TYPES and replications_int < 3:
            add(
                "major",
                "SIMULATION_REPLICATIONS_LOW",
                "Stochastic, learning, replay, or testbed studies normally require at least three independent replications/scenarios.",
            )

    matched_baselines = validation.get("matched_baselines")
    held_out_axes = validation.get("held_out_axes")
    if claim_type in PERFORMANCE_CLAIMS and _missing(matched_baselines):
        add("blocking", "MATCHED_BASELINES_MISSING", "List fair, budget-matched baselines.")
    if claim_type in {"numerical_method", "control_performance", "parameter_recovery"} and not _bool(
        validation.get("independent_solver_or_oracle")
    ):
        add("major", "INDEPENDENT_CHECK_MISSING", "Add an independent solver, rollout, oracle, or special-case check.")
    if primary_track in {"C", "D"} or claim_type in {"parameter_recovery", "predictive_generalization"}:
        if _missing(held_out_axes):
            add("blocking", "HELD_OUT_VALIDATION_MISSING", "Hold out complete time, node, host, graph, capture, or scenario axes.")
    if primary_track in {"B", "C", "D", "E"} and not _bool(validation.get("uncertainty_reported")):
        add("major", "UNCERTAINTY_MISSING", "Report uncertainty across runs, scenarios, fits, or measurement windows.")
    if claim_type in PERFORMANCE_CLAIMS and not _bool(validation.get("failure_cases_retained")):
        add("major", "FAILURE_CASES_NOT_RETAINED", "Retain failed, divergent, or non-improving runs.")
    if claim_type == "game_stability" and not _bool(validation.get("deviation_diagnostics")):
        add("blocking", "GAME_DEVIATION_CHECK_MISSING", "Add unilateral-deviation or independently solved best-response checks.")
    if claim_type == "parameter_recovery" or primary_track == "D":
        if not _bool(validation.get("identifiability_assessment")):
            add(
                "blocking",
                "IDENTIFIABILITY_UNCHECKED",
                "Assess structural/practical identifiability or use calibration/partial-identification wording.",
            )
    if claim_type == "operational_feasibility":
        if primary_track != "E":
            add("blocking", "OPERATIONAL_TRACK_TOO_WEAK", "Operational feasibility requires Track E as the primary evidence track.")
        if _missing(validation.get("operational_metrics")):
            add("blocking", "OPERATIONAL_METRICS_MISSING", "Record latency, overhead, action success/failure, recovery, or equivalent metrics.")
    if claim_type == "causal_effect":
        if primary_track != "E":
            add("blocking", "CAUSAL_TRACK_TOO_WEAK", "Simulation or calibration alone cannot establish a causal effect.")
        if _missing(validation.get("causal_design")) or str(validation.get("causal_design", "")).strip().lower() == "none":
            add("blocking", "CAUSAL_DESIGN_MISSING", "Specify a prospective, randomized, quasi-experimental, or other defensible causal design.")
    if _missing(validation.get("claim_scope")):
        add("blocking", "CLAIM_SCOPE_MISSING", "Write the exact evidence and counterfactual boundary for the main claim.")

    return sorted(issues, key=lambda issue: ("blocking major minor".split().index(issue.severity), issue.code))


def render_evidence_report(issues: list[EvidenceIssue], plan: dict[str, Any], source: str = "") -> str:
    """Render a human-readable audit report."""

    claim_type = str(plan.get("main_claim_type", ""))
    primary = str(plan.get("primary_evidence_track", "")).upper()
    recommendations = recommend_evidence_tracks(claim_type)
    counts = {severity: sum(issue.severity == severity for issue in issues) for severity in ("blocking", "major", "minor")}
    lines = ["# Evidence Plan Audit", ""]
    if source:
        lines.extend([f"Source: `{source}`", ""])
    lines.extend(
        [
            f"- Claim type: `{claim_type or 'missing'}`",
            f"- Primary track: `{primary or 'missing'}` — {TRACKS.get(primary, 'unknown')}",
            f"- Recommended sequence: `{', '.join(recommendations) or 'manual review'}`",
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
        for issue in subset:
            lines.append(f"- **{issue.code}** — {issue.message}")
        lines.append("")
    lines.extend(
        [
            "## Decision",
            "",
            "BLOCK until all blocking findings are resolved." if counts["blocking"] else "REVISE major findings before manuscript claims are frozen.",
            "",
        ]
    )
    return "\n".join(lines)
