"""Create a minimal, auditable IEEE research project scaffold."""

from __future__ import annotations

import json
from pathlib import Path


PROJECT_CONFIG = """project_name: {name}
target_journal: {journal}
target_journal_rules:
  official_source: TBD
  checked_date: TBD
research_question: TBD
main_claim: TBD
main_claim_type: mechanism | numerical_method | control_performance | game_stability | parameter_recovery | predictive_generalization | operational_feasibility | causal_effect | TBD
evidence:
  primary_track: A | B | C | D | E | TBD
  secondary_tracks: []
  repository_layers: []
  topology_evidence_level: T1 | T2 | T3 | T4 | T5 | not_applicable | TBD
  graph_semantics: contact | communication | influence | dependency | attack_path | other | TBD
model_resolution: TBD
solution_concept: TBD
novelty_status: not_audited
reproducibility:
  commit: TBD
  environment: TBD
  seeds: []
  data_provenance: TBD
"""

PROJECT_BRIEF = """# {name}

## Operational problem

[TBD]

## Main research question

[TBD]

## Modeling gap

[TBD]

## Strategy/solution gap

[TBD]

## Evidence-track decision

- primary track:
- repository layers:
- real topology/data/trace role:
- topology evidence level T1–T5:
- node and edge semantics:
- simulation or testbed role:
- claim boundary:

## Scope lock

- one model:
- one solution concept:
- one theorem ladder:
- one primary algorithm:
- one decisive experiment:

## Kill criteria

[TBD]
"""

MANUSCRIPT = r"""\documentclass[journal]{{IEEEtran}}

\title{{{name}}}
\author{{Author Names}}

\begin{{document}}
\maketitle

\begin{{abstract}}
[TBD: stakes, gap, model/problem, theory/algorithm, evidence track, evaluation/result, implication]
\end{{abstract}}

\begin{{IEEEkeywords}}
[TBD]
\end{{IEEEkeywords}}

\section{{Introduction}}
[TBD]

\section{{Related Work}}
[TBD]

\section{{System Model and Problem Formulation}}
[TBD]

\section{{Data and/or Simulation Contract}}
[TBD: observed, inferred, assumed, simulated, split, fidelity and claim boundaries]

\section{{Theoretical Analysis}}
[TBD]

\section{{Algorithm}}
[TBD]

\section{{Experimental Setup}}
[TBD]

\section{{Results and Discussion}}
[TBD]

\section{{Limitations}}
[TBD]

\section{{Conclusion}}
[TBD]

\end{{document}}
"""

CSV_HEADERS = {
    "literature/LITERATURE_QUEUE.csv": (
        "paper_id,title,year,venue,doi,url,fulltext_checked,closest_overlap,"
        "novelty_impact,must_cite,status\n"
    ),
    "literature/NOVELTY_MATRIX.csv": (
        "paper_id,problem,model,control_or_game,theory,algorithm,experiments,"
        "overlap,claim_impact,must_cite\n"
    ),
    "planning/CLAIM_EVIDENCE_MATRIX.csv": (
        "claim_id,claim_text,claim_type,required_evidence,current_evidence,"
        "source_or_artifact,scope,confidence,status\n"
    ),
    "planning/THEOREM_TO_CODE_MAP.csv": (
        "item_id,theorem_or_assumption,math_location,code_location,test_or_residual,status,notes\n"
    ),
    "planning/EXPERIMENT_MATRIX.csv": (
        "exp_id,research_question,claim_supported,evidence_track,repository_layers,"
        "data_or_simulation_source,independent_variables,controls,baselines,"
        "budget_and_information_fairness,metrics,held_out_axes,instances,"
        "seeds_or_scenarios,uncertainty,failure_case,artifact,status\n"
    ),
    "planning/EMPIRICAL_CLAIM_LEDGER.csv": (
        "claim_id,claim_text,claim_type,evidence_track,data_or_simulation_source,"
        "observed_or_counterfactual,held_out_evidence,uncertainty,claim_boundary,"
        "figure_or_table,status\n"
    ),
    "planning/FIGURE_TABLE_PLAN.csv": (
        "item_id,type,claim,evidence_track,"
        "observed_inferred_assumed_simulated_or_counterfactual,comparison,x_axis,y_axis,"
        "instances_or_split,uncertainty,claim_boundary,source_data,generation_command,status\n"
    ),
    "results/RESULTS_LOG.csv": (
        "run_id,date,commit,repository_source_commits,config,data_or_topology_version_hash,"
        "simulator_or_testbed_id,seed_or_scenario,split,environment,metric,value,unit,"
        "uncertainty,figure_or_table,interpretation,claim_boundary,limitations,status\n"
    ),
    "data/DATA_TO_MODEL_MAP.csv": (
        "map_id,dataset_id,raw_field_or_event,transformation,model_object_type,"
        "model_object,unit,time_scale,observed_or_inferred,justification,uncertainty,"
        "leakage_risk,status\n"
    ),
    "data/REAL_DATA_SPLIT_PLAN.csv": (
        "split_id,dataset_id,axis,train_or_calibration,validation,test,exclusion_rule,"
        "preprocessing_fit_scope,leakage_check,claim_supported,status\n"
    ),
    "data/REALITY_LEDGER.csv": (
        "item_id,quantity_or_event,category,source,transformation,uncertainty,"
        "used_in_model_or_claim,claim_boundary,status\n"
    ),
    "data/DATASET_DECISION_MATRIX.csv": (
        "candidate_id,dataset_name,official_source,scientific_role,model_mapping_quality,"
        "temporal_support,topology_support,labels_or_outcomes,licence_status,privacy_risk,"
        "leakage_risk,holdout_feasibility,selected,reason,status\n"
    ),
    "topology/TOPOLOGY_SOURCE_SCREENING.csv": (
        "candidate_id,domain,provider,dataset_or_graph,official_url,node_semantics,edge_semantics,"
        "directed,weighted,temporal,signed,multilayer,access_method,licence_status,privacy_risk,"
        "version_or_date,expected_size,model_compatibility,selected,rejection_reason,status\n"
    ),
    "topology/GRAPH_PREPROCESSING_LOG.csv": (
        "step_id,input_artifact,input_hash,operation,parameters,output_artifact,output_hash,"
        "nodes_before,edges_before,nodes_after,edges_after,validation_check,result,status\n"
    ),
    "topology/GRAPH_BENCHMARK_MATRIX.csv": (
        "graph_id,source_type,evidence_level,source_or_generator,version_hash,scientific_role,"
        "directed,weighted,temporal,nodes,edges,density,mean_degree,max_degree,clustering,"
        "assortativity,modularity,spectral_radius,preprocessing,normalization,split_role,"
        "graph_seed,parameter_seed,claim_supported,status\n"
    ),
    "topology/GRAPH_SPLIT_PLAN.csv": (
        "split_id,topology_id,independent_unit,train_or_design,validation,test,exclusion_rule,"
        "preprocessing_fit_scope,leakage_check,claim_supported,status\n"
    ),
    "topology/GRAPH_TO_MODEL_MAP.csv": (
        "map_id,topology_id,raw_node_or_edge_field,transformation,model_object,semantics,unit,"
        "observed_derived_or_synthetic,uncertainty,validation_check,status\n"
    ),
    "simulation/PARAMETER_PRIOR_REGISTRY.csv": (
        "parameter_id,model_parameter,unit,role,provenance_category,source_or_generator,"
        "distribution_or_range,transformation,seed,matched_mean_baseline,uncertainty,"
        "sensitivity_range,status\n"
    ),
    "simulation/NODE_LEVEL_EXPERIMENT_MATRIX.csv": (
        "exp_id,claim_id,topology_id,graph_family_or_source,graph_seed,graph_size,"
        "parameter_profile,parameter_seed,initial_state_rule,attack_seed_rule,"
        "controller_or_policy,opponent_or_environment,budget,information_structure,"
        "simulator_type,replications,baselines,metrics,held_out_axis,uncertainty,"
        "failure_policy,artifact,status\n"
    ),
    "simulation/SIMULATOR_VALIDATION_MATRIX.csv": (
        "check_id,simulator_id,check_type,reference,configuration,metric,tolerance,result,"
        "seed_or_instance,artifact,claim_impact,status\n"
    ),
    "repo_bridge/REPOSITORY_EVIDENCE_MAP.csv": (
        "item_id,project_claim,repository_layer,source_repo,source_path,source_commit,"
        "derived_rule_or_interface,project_artifact,test_or_evidence,licence_reviewed,status\n"
    ),
}


def _evidence_plan(name: str) -> str:
    payload = {
        "schema_version": 1,
        "project_name": name,
        "main_claim_type": "control_performance",
        "main_claim_statement": "TBD",
        "primary_evidence_track": "B",
        "secondary_evidence_tracks": ["A"],
        "repository_layers": ["foundation", "game_learning"],
        "data": {
            "uses_real_topology": False,
            "uses_real_traces": False,
            "uses_real_data": False,
            "topology_evidence_level": "T1",
            "topology_cards": ["topology/TOPOLOGY_CARD.yaml"],
            "dataset_cards": [],
            "data_to_model_map": "data/DATA_TO_MODEL_MAP.csv",
            "reality_ledger": "data/REALITY_LEDGER.csv",
            "adapter_contracts": ["data/ADAPTER_CONTRACT.yaml"],
            "license_checked": False,
            "version_or_hash_recorded": False,
            "privacy_ethics_checked": False,
            "split_strategy": "TBD",
            "leakage_audit": False,
        },
        "simulation": {
            "uses_simulation": True,
            "simulator_type": "sampled_closed_loop",
            "state_action_timing_defined": False,
            "verification_checks": [],
            "validation_target": "TBD",
            "replications": 0,
            "common_random_numbers": False,
            "fidelity_boundary": "TBD",
            "counterfactual_assumptions": "TBD",
            "synthetic_scenario_spec": "simulation/SYNTHETIC_SCENARIO_SPEC.yaml",
            "node_level_experiment_matrix": "simulation/NODE_LEVEL_EXPERIMENT_MATRIX.csv",
        },
        "validation": {
            "independent_solver_or_oracle": False,
            "matched_baselines": [],
            "held_out_axes": [],
            "uncertainty_reported": False,
            "failure_cases_retained": False,
            "deviation_diagnostics": False,
            "identifiability_assessment": False,
            "operational_metrics": [],
            "causal_design": "none",
            "claim_scope": "TBD",
        },
    }
    return json.dumps(payload, indent=2) + "\n"


DATASET_CARD = """schema_version: 1
dataset_id: TBD
canonical_title: TBD
provider: TBD
official_url: TBD
accessed_date: TBD
version: TBD
doi_or_citation: TBD
local_checksum: TBD
licence_or_terms: TBD
redistribution_allowed: TBD
entities: []
units: []
time_fields: []
labels: []
collection_environment: TBD
sampling_process: TBD
privacy_or_sensitive_fields: []
intended_roles: []
claim_supported: TBD
claims_not_supported: []
"""

SIMULATION_CONTRACT = """schema_version: 1
simulator_id: TBD
simulator_type: sampled_closed_loop
canonical_model_source: TBD
state_order: []
state_units: []
actions: []
action_units: []
observation_model: TBD
event_order: TBD
flow_step_or_event_clock: TBD
impulse_or_reset_map: TBD
topology_source: TBD
exogenous_event_source: TBD
random_components: []
seeds: []
replications: TBD
common_random_numbers: false
verification_checks: []
validation_target: TBD
fidelity_boundary: TBD
counterfactual_assumptions: TBD
matched_policy_information: TBD
matched_budget: TBD
failure_logging: TBD
repository_commit: TBD
"""

ADAPTER_CONTRACT = """schema_version: 1
adapter_id: TBD
adapter_role: graph | trace | observation | telemetry | testbed | TBD
input_dataset_id: TBD
input_files_or_tables: []
input_schema: []
output_model_objects: []
unit_conversions: []
time_alignment: TBD
node_or_entity_alignment: TBD
missingness_handling: TBD
label_visibility_policy: TBD
fit_scope: training_only | none | TBD
future_information_blocked: TBD
validation_checks: []
failure_policy: TBD
source_commit: TBD
licence_reviewed: TBD
"""


TOPOLOGY_CARD = """{
  "schema_version": 1,
  "topology_id": "TBD",
  "topology_evidence_level": "T1",
  "scientific_role": "contact | communication | influence | dependency | attack_path | other | TBD",
  "source_type": "observed | temporal_observed | statistic_matched | synthetic | TBD",
  "source_name": "TBD",
  "official_url": "TBD",
  "citation": "TBD",
  "licence_or_terms": "TBD",
  "license_checked": false,
  "version_or_hash": "TBD",
  "version_or_hash_recorded": false,
  "graph": {
    "node_unit": "TBD",
    "edge_unit": "TBD",
    "directed": false,
    "weighted": false,
    "signed": false,
    "temporal": false,
    "multilayer": false,
    "adjacency_semantics": "A[i,j] means j influences i",
    "self_loop_policy": "TBD",
    "parallel_edge_policy": "TBD",
    "isolated_node_policy": "TBD",
    "component_policy": "TBD",
    "weight_transformation": "none | TBD",
    "normalization": "none | row | max-degree | spectral | other | TBD",
    "timestamp_handling": "not_applicable | TBD",
    "node_attribute_provenance": "none | TBD"
  },
  "preprocessing": {
    "script": "TBD",
    "deterministic": false,
    "raw_immutable_copy": false,
    "statistics_before": {},
    "statistics_after": {},
    "validation_checks": []
  },
  "synthetic_design": {
    "generator_families": [],
    "generator_parameters": {},
    "target_observed_statistics": [],
    "goodness_of_match": "not_applicable | TBD",
    "graph_seeds": []
  },
  "split": {
    "claims_topology_generalization": false,
    "strategy": "not_applicable | TBD",
    "held_out_graphs_or_snapshots": [],
    "leakage_audit": false
  },
  "model_mapping": {
    "state_resolution": "node_level",
    "graph_to_model_map": "topology/GRAPH_TO_MODEL_MAP.csv",
    "dynamics_observed_or_synthetic": "synthetic | calibrated | observed | mixed | TBD",
    "parameter_provenance": "TBD",
    "attack_seed_rules": []
  },
  "validation": {
    "matched_topology_controls": [],
    "independent_solver_or_stochastic_ensemble": false,
    "topology_perturbations": [],
    "multiple_graph_instances": false,
    "failure_cases_retained": false
  },
  "claim_boundary": "TBD",
  "claims_not_supported": []
}
"""

TOPOLOGY_ACQUISITION = """# Topology Acquisition Plan

## Scientific edge semantics

[TBD: what does a node represent; what does an edge represent; why is this topology compatible with the state equation, simulator or attack path?]

## Candidate screening

Complete `TOPOLOGY_SOURCE_SCREENING.csv` before selecting a graph. Search official providers and primary dataset repositories rather than reposted mirrors.

| Candidate | Official source | Node/edge semantics | Direction/weight/time | Terms/privacy | Compatibility | Decision |
|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD |

Record a rejection reason for every plausible candidate that is not used. Availability alone is not scientific compatibility.

## Acquisition and immutable raw copy

[TBD: lawful access route, retrieval date, version, checksum, private/raw storage location, redistribution boundary.]

## Deterministic preprocessing

[TBD: script, self-loop/duplicate/component/isolate policy, identifiers, direction, weight transformation, temporal windowing, normalization.]

## Validation against source statistics

[TBD: node/edge counts, degree distribution, components, clustering, assortativity, modularity, spectral radius, time coverage, and source-published statistics where available.]

## Split/holdout plan

[TBD: complete graph, snapshot, scenario, community, node/time masks; explain how graph, temporal and entity leakage are prevented.]

## Matched synthetic controls

[TBD: graph families or configuration-model controls; matched density/mean degree/degree sequence/community statistics; generator seeds and goodness-of-match.]

## Reality and claim boundary

[TBD: distinguish observed topology and attributes from calibrated, assumed, synthetic and counterfactual dynamics, parameters, attacks and interventions.]
"""

SYNTHETIC_SCENARIO_SPEC = """{
  "schema_version": 1,
  "scenario_id": "TBD",
  "scientific_question": "TBD",
  "graph": {
    "topology_id": "TBD",
    "source": "observed | generated | statistic_matched | TBD",
    "family": "TBD",
    "seed": "TBD",
    "nodes": "TBD",
    "directed": "TBD",
    "weighted": "TBD",
    "parameters": {}
  },
  "dynamics": {
    "model": "TBD",
    "parameter_profile": "TBD",
    "parameter_seed": "TBD",
    "initial_state_rule": "TBD",
    "attack_seed_rule": "TBD"
  },
  "decision": {
    "information_structure": "TBD",
    "action_timing": "TBD",
    "budget": "TBD",
    "horizon": "TBD"
  },
  "simulation": {
    "type": "ode | gillespie | monte_carlo | agent_based | event_driven | sampled_closed_loop | hybrid | TBD",
    "numerical_settings": {},
    "replications": 0,
    "common_random_numbers": false
  },
  "validation": {
    "independent_check": "TBD",
    "invariants": [],
    "failure_policy": "TBD"
  }
}
"""

THEOREM_PROOF_CHECKLIST = """# Theorem and Proof Checklist

- [ ] statement and scope
- [ ] assumptions and dependencies
- [ ] necessary versus sufficient status
- [ ] proof or cited result
- [ ] implementation/test mapping
- [ ] limitations and counterexample search
"""

STYLE_CONFLICT_LOG = """# Style Conflict Log

Record any place where author-style preferences are overridden by evidence, clarity, discipline, or target-journal convention.
"""

RESPONSE_TO_REVIEWERS = """# Response to Reviewers

For every comment: diagnosis → action → evidence → manuscript location → concise response.
"""


TRACE_REPLAY = """# Trace-Replay Plan

## Trace and scenario unit

[TBD]

## Field/event to simulator role

[TBD]

## Replay and action timing

[TBD]

## Split and leakage controls

[TBD]

## Counterfactual response assumptions

[TBD]

## Fidelity and claim boundary

[TBD]
"""


ASSET_TEMPLATE_TARGETS = {
    "ADAPTER_CONTRACT.yaml": "data/ADAPTER_CONTRACT.yaml",
    "CALIBRATION_VALIDATION_PLAN.md": "data/CALIBRATION_VALIDATION_PLAN.md",
    "CLAIM_EVIDENCE_MATRIX.csv": "planning/CLAIM_EVIDENCE_MATRIX.csv",
    "DATASET_CARD.yaml": "data/DATASET_CARD.yaml",
    "DATASET_DECISION_MATRIX.csv": "data/DATASET_DECISION_MATRIX.csv",
    "DATA_TO_MODEL_MAP.csv": "data/DATA_TO_MODEL_MAP.csv",
    "EMPIRICAL_CLAIM_LEDGER.csv": "planning/EMPIRICAL_CLAIM_LEDGER.csv",
    "EVIDENCE_PLAN.json": "evidence/EVIDENCE_PLAN.json",
    "EXPERIMENT_MATRIX.csv": "planning/EXPERIMENT_MATRIX.csv",
    "FIGURE_TABLE_PLAN.csv": "planning/FIGURE_TABLE_PLAN.csv",
    "FULL_CORPUS_STATUS.csv": "literature/FULL_CORPUS_STATUS.csv",
    "GRAPH_BENCHMARK_MATRIX.csv": "topology/GRAPH_BENCHMARK_MATRIX.csv",
    "GRAPH_PREPROCESSING_LOG.csv": "topology/GRAPH_PREPROCESSING_LOG.csv",
    "GRAPH_SPLIT_PLAN.csv": "topology/GRAPH_SPLIT_PLAN.csv",
    "GRAPH_TO_MODEL_MAP.csv": "topology/GRAPH_TO_MODEL_MAP.csv",
    "LITERATURE_QUEUE.csv": "literature/LITERATURE_QUEUE.csv",
    "MANUSCRIPT_OUTLINE.md": "manuscript/OUTLINE.md",
    "NODE_LEVEL_EXPERIMENT_MATRIX.csv": "simulation/NODE_LEVEL_EXPERIMENT_MATRIX.csv",
    "NOVELTY_MATRIX.csv": "literature/NOVELTY_MATRIX.csv",
    "PAPER_CARD_TEMPLATE.md": "literature/PAPER_CARD_TEMPLATE.md",
    "PARAMETER_PRIOR_REGISTRY.csv": "simulation/PARAMETER_PRIOR_REGISTRY.csv",
    "PROJECT_BRIEF.md": "PROJECT_BRIEF.md",
    "PROJECT_CONFIG.yaml": "PROJECT_CONFIG.yaml",
    "REALITY_LEDGER.csv": "data/REALITY_LEDGER.csv",
    "REAL_DATA_SPLIT_PLAN.csv": "data/REAL_DATA_SPLIT_PLAN.csv",
    "REPOSITORY_EVIDENCE_MAP.csv": "repo_bridge/REPOSITORY_EVIDENCE_MAP.csv",
    "RESPONSE_TO_REVIEWERS.md": "manuscript/RESPONSE_TO_REVIEWERS.md",
    "RESULTS_LOG.csv": "results/RESULTS_LOG.csv",
    "SIMULATION_CONTRACT.yaml": "simulation/SIMULATION_CONTRACT.yaml",
    "SIMULATOR_VALIDATION_MATRIX.csv": "simulation/SIMULATOR_VALIDATION_MATRIX.csv",
    "STYLE_CONFLICT_LOG.md": "planning/STYLE_CONFLICT_LOG.md",
    "SYNTHETIC_SCENARIO_SPEC.yaml": "simulation/SYNTHETIC_SCENARIO_SPEC.yaml",
    "THEOREM_PROOF_CHECKLIST.md": "planning/THEOREM_PROOF_CHECKLIST.md",
    "THEOREM_TO_CODE_MAP.csv": "planning/THEOREM_TO_CODE_MAP.csv",
    "TOPOLOGY_ACQUISITION_PLAN.md": "topology/TOPOLOGY_ACQUISITION_PLAN.md",
    "TOPOLOGY_CARD.yaml": "topology/TOPOLOGY_CARD.yaml",
    "TOPOLOGY_SOURCE_SCREENING.csv": "topology/TOPOLOGY_SOURCE_SCREENING.csv",
    "TRACE_REPLAY_PLAN.md": "simulation/TRACE_REPLAY_PLAN.md",
}


def _asset_template_root() -> Path | None:
    for parent in Path(__file__).resolve().parents:
        candidate = parent / "assets/templates"
        if (parent / "SKILL.md").is_file() and candidate.is_dir():
            return candidate
    return None


def _render_asset_template(filename: str, text: str, name: str, journal: str) -> str:
    if filename == "PROJECT_CONFIG.yaml":
        text = text.replace("project_name: TBD", f"project_name: {name}", 1)
        text = text.replace("target_journal: TIFS", f"target_journal: {journal}", 1)
    elif filename == "EVIDENCE_PLAN.json":
        text = text.replace('"project_name": "TBD"', f'"project_name": {json.dumps(name)}', 1)
    elif filename == "PROJECT_BRIEF.md":
        text = text.replace("# Project Brief", f"# {name} — Project Brief", 1)
    return text


def _canonical_template_files(name: str, journal: str) -> dict[str, str]:
    root = _asset_template_root()
    if root is None:
        return {}
    files: dict[str, str] = {}
    for filename, target in ASSET_TEMPLATE_TARGETS.items():
        source = root / filename
        if not source.is_file():
            raise FileNotFoundError(f"Missing canonical project template: {source}")
        files[target] = _render_asset_template(filename, source.read_text(encoding="utf-8"), name, journal)
    return files


def create_project(name: str, journal: str, output: str | Path, force: bool = False) -> Path:
    target = Path(output)
    if target.exists() and any(target.iterdir()) and not force:
        raise FileExistsError(
            f"Output directory is not empty: {target}. Use --force to add scaffold files."
        )
    target.mkdir(parents=True, exist_ok=True)
    for directory in (
        "manuscript",
        "literature",
        "planning",
        "model",
        "src",
        "tests",
        "experiments",
        "results",
        "figures",
        "reports",
        "evidence",
        "data",
        "simulation",
        "topology",
        "repo_bridge",
    ):
        (target / directory).mkdir(exist_ok=True)

    files = {
        "PROJECT_CONFIG.yaml": PROJECT_CONFIG.format(name=name, journal=journal),
        "PROJECT_BRIEF.md": PROJECT_BRIEF.format(name=name),
        "manuscript/main.tex": MANUSCRIPT.format(name=name),
        "evidence/EVIDENCE_PLAN.json": _evidence_plan(name),
        "data/DATASET_CARD.yaml": DATASET_CARD,
        "data/ADAPTER_CONTRACT.yaml": ADAPTER_CONTRACT,
        "simulation/SIMULATION_CONTRACT.yaml": SIMULATION_CONTRACT,
        "simulation/SYNTHETIC_SCENARIO_SPEC.yaml": SYNTHETIC_SCENARIO_SPEC,
        "simulation/TRACE_REPLAY_PLAN.md": TRACE_REPLAY,
        "topology/TOPOLOGY_CARD.yaml": TOPOLOGY_CARD,
        "topology/TOPOLOGY_ACQUISITION_PLAN.md": TOPOLOGY_ACQUISITION,
        "planning/THEOREM_PROOF_CHECKLIST.md": THEOREM_PROOF_CHECKLIST,
        "planning/STYLE_CONFLICT_LOG.md": STYLE_CONFLICT_LOG,
        "manuscript/RESPONSE_TO_REVIEWERS.md": RESPONSE_TO_REVIEWERS,
        "README.md": (
            f"# {name}\n\nTarget journal: {journal}. Start with `PROJECT_BRIEF.md` and "
            "`evidence/EVIDENCE_PLAN.json`.\n"
        ),
        ".gitignore": (
            ".venv/\n__pycache__/\nreports/\nartifacts/\ndata/raw/\ndata/private/\n"
            "checkpoints/\n*.aux\n*.log\n*.out\n*.bbl\n*.blg\n"
        ),
    }
    files.update(CSV_HEADERS)
    files.update(_canonical_template_files(name, journal))
    for rel, content in files.items():
        path = target / rel
        if not path.exists() or force:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    return target
