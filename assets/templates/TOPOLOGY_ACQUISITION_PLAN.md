# Topology Acquisition Plan

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
