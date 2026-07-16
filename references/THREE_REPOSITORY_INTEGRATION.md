# Three-Repository Integration Design

## 结论

可以融入，而且不是把三份讲义简单拼接到写作 SKILL 中，而是把它们转化为一个 **模型—控制/博弈—学习—数据—验证** 的研究方法层。三仓库分别覆盖了当前包最需要补强的三个环节：

```text
mechanistic model and mathematical contract
    ↓
sampled feedback / multi-agent simulation
    ↓
partial-data estimation / physics-informed learning
```

The integration should remain **derived and modular**. The skill links to pinned repository snapshots, records which doctrine came from which file, and paraphrases the reusable research logic. It must not silently vendor tutorial text, repository code, PDFs, or generated figures.

## Layered architecture

### Layer F — Foundation

Source family: `network-control-differential-games`.

Use it to establish:

- states, units, graph resolution, controls, information, reset maps, and objective;
- aggregate/degree/node model selection;
- PMP/FBS, differential-game, impulse, and continuous-impulsive formulations;
- invariant, Jacobian, stationarity, grid, and scaling checks;
- graph and parameter provenance;
- theorem-to-code and manuscript-to-repository traceability.

### Layer G — Game and feedback learning

Source family: `note1-cyber-control-games`.

Use it to establish:

- continuous-model-to-MDP/Markov-game conversion;
- action timing and reward accounting;
- selection among discrete, parameterized, centralized, decentralized, and multi-agent methods;
- repeated simulation rollouts, held-out graph/parameter evaluation, and matched budgets;
- response matrices, unilateral deviations, and bounded game claims.

### Layer P — Physics-informed data integration

Source family: `note2-pinn-pidl-cyber-control`.

Use it to establish:

- the unknown-object declaration;
- observed data versus residual/collocation points;
- inverse estimation, missing-mechanism correction, neural control, and PMP-informed learning;
- identifiability, heterogeneous parameterization, held-out nodes/times/graphs;
- independent numerical rollout and loss-component diagnostics;
- calibration-versus-recovery claim boundaries.

## How this changes the research pipeline

The original pipeline can be strengthened as follows:

```text
operational problem
→ evidence-track selection
→ repository-layer selection
→ model/data/simulation contract
→ theory and algorithm
→ verification
→ synthetic or semi-empirical simulation
→ real-data calibration/validation where justified
→ claim-bounded IEEE Transactions manuscript
```

This avoids two common failures:

1. adding RL or PINN because it is fashionable rather than because the question requires feedback or partial data;
2. adding a “real dataset” table that is disconnected from the state variables, parameters, controls, and claims.

## Integration principle: one canonical mechanism, multiple evidence layers

A paper should maintain one canonical state equation and notation dictionary. Different repositories contribute different interfaces to that mechanism:

- Foundation: deterministic equation and solver.
- Game learning: sampled environment and policy interface.
- Physics-informed: observation/residual and estimation interface.

The interfaces may differ, but state order, units, control meaning, topology convention, parameter provenance, and objective must remain aligned. WORK must create a cross-repository consistency table for every project that uses more than one layer.

## Public-release boundary

- The Foundation repository currently has no blanket permissive licence. Public skill releases should include only owner-authored derived summaries, paths, commit identifiers, and interface specifications unless a separate licensing decision is made.
- Note 1 and Note 2 declare MIT licensing unless a file says otherwise. Even so, the skill should prefer links and adapters over vendoring because duplicated code will drift.
- No tutorial PDF, LaTeX source, generated figure, article PDF, dataset, checkpoint, or GitHub token belongs in this skill ZIP.
- Dataset licences are separate from repository licences and must be checked per dataset.

## WORK deliverables

WORK should produce or update:

1. `repo_family/repository_manifest.yaml` with refreshed commit SHAs and licence checks.
2. One derived card per repository with source-path provenance.
3. `repo_family/cross_repo_method_map.csv`.
4. A repository-to-skill traceability report identifying every SKILL rule added from the teaching family.
5. Optional adapters as separate, tested modules; no copy-paste forks of the three packages.
6. At least three end-to-end blueprints: theory + real topology, feedback simulation + traces, and real-data calibration + counterfactual control.
7. New evidence, dataset, simulation, and claim gates in `QUALITY_GATES.md`.
