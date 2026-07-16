# Lu-Xing Yang IEEE Transactions Research Skill

**Language: [简体中文](README.md) | English**

A Codex skill for the full IEEE Transactions research workflow, encoding **Lu-Xing Yang's personal research directions, argument structure, writing preferences, and evidence thresholds**.

> [!IMPORTANT]
> **This is not a universal IEEE writing template.**
>
> The skill is deliberately opinionated. It favors operational cybersecurity decision problems that progress through mechanism modeling, control or game-theoretic formalization, theoretical conditions, reproducible algorithms, and layered evidence before reaching carefully bounded conclusions. It actively narrows topics that are too broad, preserves adverse evidence, sets `GO / NO-GO` gates, and rejects unsupported claims such as “first,” “optimal,” “significant,” “robust,” or “practical.”
>
> If your research paradigm, target venue, evidence standards, or writing habits differ, treat this as an optional personalized framework—not a rulebook that every researcher should copy.

## What This Is

This skill is not merely a prompt for polishing prose. It is an executable personal research workflow:

```text
operational problem
→ full-text novelty boundary
→ minimal model and solution notion
→ theorem / algorithm / estimator
→ adequate evidence track
→ reproducible results
→ calibrated IEEE prose
→ claim-by-claim preflight
```

It is designed for work targeting TIFS, TDSC, TSMC, TNSE, and TCSS, covering research-direction planning, full-text novelty audits, mathematical derivation, experiments and simulation, manuscript writing, pre-submission checks, and reviewer responses.

## What Makes It Strongly Personal

- **Problem-driven, not module-stacked.** Lock the decision maker, actions, costs, information, budget, and outcome before deciding whether data, neural networks, extra players, or additional theorems are necessary.
- **Mechanism and intervention gaps.** Separate what existing models cannot represent from what existing methods cannot decide.
- **Explicit formal objects.** Prefer to name and define the model, problem, optimality system, equilibrium concept, algorithm, or estimator.
- **Theory–code–evidence closure.** Map assumptions, equations, constraints, resets, and theorem conditions to the implementation, tests, and stated limitations.
- **Evidence before claims.** Require matched baselines, independent checks, repeated experiments, uncertainty quantification, sensitivity analysis, failure logs, and reproducible configurations.
- **Calibrated conclusions.** Accept negative results, narrower claims, and `NO-GO` decisions rather than hiding adverse evidence to make a paper appear stronger.
- **Personal style as a soft constraint.** Factual accuracy, mathematical correctness, copyright and ethics, and current journal requirements always override stylistic preferences.

## Who It Fits—and Who May Not Want to Copy It Directly

| Better fit | May not fit directly |
|---|---|
| Cyber-threat propagation, malware, and APT defense | Topics weakly connected to networks, dynamic decisions, or formal validation |
| Optimal control, impulse/hybrid control, and differential games | Research paradigms based primarily on qualitative narrative |
| Stackelberg, coalition, repeated, or multi-agent games | Workflows focused only on generating fluent text without evidence gates |
| Network topology, heterogeneity, and node-level simulation | Projects that expect to inherit strong “first,” “optimal,” or “real-world” claims automatically |
| Mechanism-grounded RL/MARL/MPC and PINN/PIDL extensions | Projects unwilling to accept negative results, scope reduction, or `NO-GO` judgments |
| IEEE Transactions work emphasizing theory–algorithm–experiment consistency | Authorial styles that differ substantially from Lu-Xing Yang's research structure |

## Personal Research Portfolio

### Established Core

- Spreading dynamics, thresholds, and stability analysis;
- Malware, IoT threats, and APT defense;
- Optimal control, differential games, and strategic interaction;
- Patching, quarantine, backup, recovery, and cost-effective decision making.

### Current Expansion

- Impulse and hybrid control;
- Coupled cyber propaganda, rumor, awareness, and opinion dynamics;
- Social-engineering malware;
- Employee security compliance, incentive–audit mechanisms, and hierarchical Stackelberg decisions;
- Node-level counterfactual simulation on observed topologies.

### Capabilities Added Cautiously

- RL, MARL, self-play, and MPC;
- Hybrid attack-graph and spreading-dynamics models;
- PINNs, PIDL, inverse problems, and missing-mechanism learning;
- Real-data calibration, cyber ranges, emulation, and hardware-in-the-loop evidence.

These capabilities are added only when the research question and available data genuinely require them. They are not decorative “innovation modules.”

## What It Can Do

| Task | Typical outputs |
|---|---|
| Analyze a new direction or research package | Scope lock, research questions, claims, evidence track, termination conditions |
| Conduct a full-text novelty audit | Closest-work matrix, adverse evidence, must-cite list, claim reduction |
| Build and derive a mathematical model | State/unit/information contracts, theorem dependencies, optimality or equilibrium conditions |
| Design experiments and simulations | Topology cards, baselines, seed/parameter matrices, independent solver checks |
| Write an IEEE manuscript | Abstract, Introduction, contribution chain, methods, results, and limitations |
| Run a pre-submission audit | Claim–evidence alignment, overclaiming, theory–code drift, privacy and copyright checks |
| Prepare reviewer responses | Comment–action–evidence ledger, point-by-point responses, residual risks |

## Quick Installation

This is a public repository. For a fresh installation, clone it directly into the Codex skills directory:

```bash
git clone https://github.com/LYang910920/luxing-ieee-transactions-skill.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/luxing-ieee-transactions"
```

If that directory already exists, use `git pull --ff-only` only when it is a Git worktree with no local changes you need to preserve. Otherwise back up the old directory before reinstalling so personal edits are not silently overwritten.

After installation, invoke the skill in natural language, for example:

```text
Use $luxing-ieee-transactions to start a new TIFS research direction.
Using my paper style, analyze this direction and define its GO / NO-GO conditions.
Following my TIFS style, conduct a full-text novelty audit before derivation and simulation.
Check whether this manuscript closes the theory–code–evidence loop.
Design an IEEE Transactions structure and experiment plan for this Stackelberg differential-game paper.
```

## Evidence Basis and Boundaries

The current version is `v0.4.0`, with status `expanded-partial-calibration`:

- 73 verified full texts were deep-read paper by paper: 42 owner-provided papers plus 31 nonduplicate open-access journal articles;
- The expanded 73-paper set informs research architecture, mathematical and algorithmic correction gates, experiment consistency, and claim boundaries;
- Sentence-level personal-style metrics remain anchored to the role-weighted 42-paper local corpus, including a 20-paper first/corresponding-author core-voice subset;
- 17 IEEE Transactions full texts informed venue structure and research architecture;
- All 17 owner-priority Transactions records currently have private full text;
- One paper from a different technical subfield is explicitly owner-deprioritized.

> [!NOTE]
> The 73 papers form a verified-full-text deep-reading working corpus, not a proven complete publication universe. Open access and coauthorship do not automatically establish personal sentence-level authorship; papers without verified writing roles mainly inform research architecture, correction rules, method combinations, and experimental design.

The repository retains only bibliographic metadata, aggregate counts, hashes, stable derived rules, derived metrics, and paraphrased paper cards. It **does not contain article PDFs, per-paper deep-reading notes, extracted article text, copied figures, tables, or equations, Deakin downloads, or other restricted source materials**.

## Evidence Tracks

| Track | Primary evidence | Default claim boundary |
|---|---|---|
| A | Mechanistic model, formal results, verified numerics | Behavior and conditions under stated assumptions |
| B | Stochastic, agent-based, event-driven, or closed-loop simulation | Distributional policy behavior under simulator assumptions |
| C | Observed topology or trace with simulated/counterfactual dynamics | Sensitivity to observed structure or recorded conditions |
| D | Real-data calibration and held-out prediction | Fit, effective-rate estimation, and prediction under an observation model |
| E | Cyber range, emulation, hardware-in-the-loop, or field evidence | Bounded feasibility and measured operational behavior |

Observed topology with synthetic spreading is only `real-topology simulation`; it is not real-world validation.

## Repository Map

- [`SKILL.md`](SKILL.md): Codex runtime entry point and routing logic.
- [`references/PERSONAL_RESEARCH_DIRECTIONS.md`](references/PERSONAL_RESEARCH_DIRECTIONS.md): Personal research directions and maturity levels.
- [`references/PERSONAL_STYLE_PROFILE.md`](references/PERSONAL_STYLE_PROFILE.md): Personal writing and argumentation profile.
- [`references/RESEARCH_PIPELINE.md`](references/RESEARCH_PIPELINE.md): End-to-end research workflow.
- [`references/QUALITY_GATES.md`](references/QUALITY_GATES.md): Theory, algorithm, evidence, and claim gates.
- [`references/FULLTEXT_CORPUS_DERIVED_DOCTRINE.md`](references/FULLTEXT_CORPUS_DERIVED_DOCTRINE.md): Mechanism, theorem, solver, experiment, and claim-consistency doctrine derived from the 73 full-text readings.
- [`references/corpus/open_access_fulltext_manifest.csv`](references/corpus/open_access_fulltext_manifest.csv): Public bibliographic boundary for the 31-paper open-access expansion.
- [`references/THIRD_PARTY_NOTICES.md`](references/THIRD_PARTY_NOTICES.md): Copyright, paper, and third-party material boundaries.
- [`assets/templates/`](assets/templates/): Project, evidence, data, topology, and manuscript templates.
- [`scripts/luxing_ieee.py`](scripts/luxing_ieee.py): Validation, preflight, scaffolding, and evidence-recommendation tools.

## Local Validation

```bash
SKILL_DIR="${CODEX_HOME:-$HOME/.codex}/skills/luxing-ieee-transactions"
python "$SKILL_DIR/scripts/luxing_ieee.py" validate
python "$SKILL_DIR/scripts/validate_skill.py" --json
```

## Operating Principles

1. Do not place historical personal habits above factual accuracy, mathematical correctness, or current journal requirements.
2. Do not imitate historical grammar flaws or mechanically repeat familiar transitions.
3. Do not interpret coauthorship as personal ownership of sentence-level style.
4. Do not present observed topology as field validation, synthetic recovery as field calibration, or a single converged run as global optimality.
5. Do not hide adverse literature, failed experiments, non-identifiability, or results that invalidate the direction.

## License

The skill workflow and original templates are licensed under [`LICENSE`](LICENSE). Papers, datasets, teaching repositories, and other third-party materials remain subject to their respective rights and licenses; this repository does not relicense them.

---

**中文说明：** 这是一个带有强烈个人研究风格的 IEEE Transactions 全流程 Codex SKILL，强调网络安全决策、机制建模、控制与博弈、理论—代码—证据闭环以及有边界的学术表述。它并非适用于所有研究者或论文的通用模板。
