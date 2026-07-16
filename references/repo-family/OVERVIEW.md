# Three-Repository Teaching-Family Integration

This directory records a **derived, non-copying integration layer** for Lu-Xing Yang's three GitHub teaching repositories. It does not vendor their code, tutorial PDFs, LaTeX sources, figures or datasets.

The repositories play complementary roles:

1. `network-control-differential-games` supplies the mechanistic model, control/game formulation, graph inputs, FBS solvers, invariants and numerical baselines.
2. `note1-cyber-control-games` supplies the conversion from continuous dynamics to sampled environments or Markov games, feedback learning, multi-agent evaluation and game-deviation diagnostics.
3. `note2-pinn-pidl-cyber-control` supplies inverse estimation, physics-informed learning, missing-mechanism modelling, neural control and independent rollout validation.

The skill consumes **methodological doctrines and interfaces**, not lecture prose. Before WORK derives or updates any card, it must pin the current commit, read the applicable licence/notice and record source paths.

Files:

- `repository_manifest.yaml` — source repositories, commits, canonical paths and licence boundaries;
- `foundation_card.md` — mechanism/numerics layer;
- `game_learning_card.md` — feedback/game simulation layer;
- `physics_informed_card.md` — calibration/physics-informed layer;
- `cross_repo_method_map.csv` — question/data/decision to method/layer mapping;
- `derived_doctrine_trace.csv` — each SKILL doctrine traced to source path and commit;
- `../references/THREE_REPOSITORY_INTEGRATION.md` — integration design;
- `../references/ADAPTER_ARCHITECTURE.md` — real topology, trace, observation and testbed adapter contracts.
