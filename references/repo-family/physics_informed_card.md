# Repository Card — Physics-Informed Cyber Control

## Role in the skill

Use this repository when the paper has partial observations, unknown parameters, hidden states, missing mechanisms, learned controls, or an optimality system approximated by neural networks.

## Stable doctrines to integrate

- Begin with the sentence: “The unknown object is …”. Network outputs and loss terms follow from that declaration.
- Separate observed data points from collocation/residual points.
- Validate the mechanistic model and NumPy/Torch consistency before fitting a network.
- Log data, residual, initial/boundary, constraint, and regularization losses separately.
- Hold out nodes, times, trajectories, or graphs from every training loss.
- Use an identifiable parameterization; do not fit one global rate to heterogeneous truth and describe it as local recovery.
- Validate learned parameters or controls with independent numerical rollouts, not only neural-network outputs.
- Separate residual consistency, parameter recovery, interpolation, generalization, mechanism discovery, and control performance claims.

## Route to real-data integration

The current maintained examples generate controlled synthetic truth, which is appropriate for recovery tests because the parameters are known. To use real data, WORK must add a data adapter and explicitly distinguish:

- observed variables versus latent compartments;
- timestamp, node, and trajectory masks;
- measurement units and aggregation windows;
- known versus estimated parameters;
- identifiability assumptions and priors;
- temporal/node/topology holdouts;
- independent forecast or rollout validation.

A real dataset normally does not provide “true” propagation parameters. Parameter recovery language must therefore be replaced by calibration, effective-rate estimation, predictive validation, or partial-identification language unless an independent ground truth exists.

## Skill integration points

- Data-to-model map.
- Dataset card and split plan.
- Identifiability audit.
- Calibration-versus-recovery claim gate.
- Missing-mechanism ablation ladder.
- Independent rollout and residual-map validation.
- Hybrid pipeline: real data calibrates a mechanistic model; the calibrated simulator then supports control or game experiments with explicit counterfactual limits.
