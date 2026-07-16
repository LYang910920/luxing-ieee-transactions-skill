# Candidate Real Datasets and Their Proper Roles

Prepared from official provider pages on 2026-07-15. This is a **screening registry**, not an instruction to download or use every dataset. WORK must recheck the official page, licence, citation, access, size, and suitability before use.

## 1. Stanford SNAP network collection

Official source: `https://snap.stanford.edu/data/`

Relevant roles:

- **Real topology:** communication, social, Internet, autonomous-system, web, signed, and computer-communication graphs.
- **Temporal topology/trace:** timestamped email, online interaction, signed trust, and activity networks.
- **Information diffusion:** Higgs Twitter, Memetracker, Reddit hyperlinks, and other temporal/social collections.

Potential project examples:

| Domain | Candidate examples | Intended role |
|---|---|---|
| Cyber/network control | `cisco-secure-workload`, `as-733`, `as-Skitter`, `p2p-Gnutella` | real communication/Internet topology |
| APT/malware propagation | `email-Eu-core`, `email-Enron`, computer-communication networks | contact/influence topology only unless event semantics are justified |
| Propaganda/opinion | `higgs-twitter`, `soc-RedditHyperlinks`, `memetracker9`, `wiki-Talk` | real diffusion/interaction topology or temporal activity |
| Trust/adversarial influence | `soc-sign-bitcoin-*`, `soc-sign-epinions`, signed Slashdot | signed/weighted influence topology |

Claim boundary:

A SNAP graph makes the topology empirical; it does not make infection, belief-transition, cost, or control parameters empirical. Check the individual dataset page for terms and citation requirements.

## 2. UNSW-NB15

Official source: `https://research.unsw.edu.au/projects/unsw-nb15-dataset`

Provider description relevant to study design:

- raw packet, Bro/Zeek, Argus, CSV, and report files;
- traffic generated in the UNSW Canberra Cyber Range;
- hybrid real modern normal activity and synthetic attack behavior;
- nine attack categories;
- official training and testing partitions are available.

Good roles in this skill:

- define attack-event intensity or scenario mix;
- define an observation/IDS error model;
- trace-driven stress of a defense policy;
- compare temporal or host-level shifts;
- calibrate exogenous attack modes, not automatically propagation rates.

Do not claim:

- field malware prevalence;
- natural operational intervention effects;
- real propagation ground truth merely because packet data are real/cyber-range generated.

## 3. TON_IoT

Official source: `https://research.unsw.edu.au/projects/toniot-datasets`

Provider description relevant to study design:

- heterogeneous telemetry, Windows/Linux operating-system, and network-traffic data;
- IoT/IIoT, edge/fog/cloud testbed;
- raw, processed, train/test, descriptive-statistics, and security-event-ground-truth folders;
- event timestamps and multiple attack types;
- the official page grants free use for academic research and requests citation of the listed papers; commercial use requires author contact.

Good roles in this skill:

- multi-modal observation model for latent compromise/risk;
- timestamped attack and normal-event replay;
- cross-source missingness and sensor ablations;
- node/device/time holdouts;
- calibration of exogenous loads, detection probabilities, or effective rates;
- testbed-informed latency/observation models.

Required cautions:

- define how telemetry and labels map to model states;
- prevent timestamp and host leakage;
- separate testbed realism from production deployment;
- record which of the four data families was used.

## 4. IoT-23

Official source: `https://www.stratosphereips.org/datasets-iot23`

Provider description relevant to study design:

- 23 IoT network-traffic captures;
- 20 malware captures and 3 benign-device captures;
- real IoT devices for benign traffic and controlled malware execution;
- packet captures and labelled Zeek connection logs;
- scenario-level metadata and a dataset DOI/citation.

Good roles in this skill:

- scenario-level trace replay;
- event-arrival and protocol-mix modeling;
- benign-versus-malicious observation/noise models;
- held-out malware family, capture, device, or time evaluation;
- stress-testing an adaptive defense simulator.

Required cautions:

- the data are flows/captures, not node-compartment trajectories by default;
- an intervention response model is needed for counterfactual policy evaluation;
- split by complete scenario/capture before feature aggregation;
- dataset size and redistribution terms must be checked before storage or sharing.

## Selection matrix

| Research object | Best first candidate | Data role | Additional model requirement |
|---|---|---|---|
| Real cyber/social topology | SNAP | topology | propagation and action parameters remain declared/calibrated |
| Cyber-range network flows | UNSW-NB15 | trace/observation/scenario | map flow events to attack process or measurements |
| Multi-modal IoT/IIoT telemetry | TON_IoT | observation/calibration/trace | latent-state and sensor model |
| IoT malware and benign captures | IoT-23 | trace replay/observation | counterfactual response model for defense actions |
| Propaganda diffusion topology/activity | SNAP temporal/social datasets | topology/activity trace | belief-state and influence model |

## Dataset admission test

A dataset may enter the paper only when all answers are explicit:

1. Which model object does it inform: topology, state, parameter, observation, action, exogenous input, or evaluation metric?
2. What unit and time scale does the mapping use?
3. Which parts are observed, inferred, assumed, or simulated?
4. What split prevents temporal, node, host, graph, or scenario leakage?
5. What claim becomes stronger because of the dataset?
6. What claim remains unsupported?
7. Are licence, citation, ethics, privacy, and redistribution requirements satisfied?
