# Current Lu-Xing Yang IEEE Transactions Style Profile

**Version:** 0.4.0
**Status:** `expanded-partial-calibration`

## Evidence base

The research doctrine now uses a verified 73-paper full-text working corpus: 42 owner-provided papers plus 31 nonduplicate open-access journal articles discovered through the owner's publication identity and verified to an actual PDF or complete publisher HTML. The 42-paper local corpus contains 17 IEEE Transactions papers, a 20-paper first/corresponding-author core-voice subset, and 19 papers from 2024 onward. The selected 18-row Transactions manifest has 17 private-full-text-covered priority rows and one explicitly deprioritized different-subfield row.

The expanded set is still not a verified complete publication universe. Sentence-level preferences remain driven by the role-weighted local corpus, especially first/corresponding-author or documented original-draft papers. The 31 open-access additions strengthen research architecture, mathematical/algorithmic quality gates, method evolution, and consistency checks; they do not automatically become personal sentence-voice evidence.

## Calibration limits

- The 20-paper core-voice tier is a weighting set, not proof that every sentence or section was personally drafted by the owner. Corresponding-author status remains a signal, and many contribution roles are still unknown.
- The expanded 73-paper deep-reading set is architecture and correction evidence. It does not change the 20-paper personal-voice core or the attachment-derived quantitative sentence targets.
- Abstract-level architecture and sentence rhythm are better supported than paragraph-level, section-specific, collaborator-specific, or punctuation-level microstyle.
- TIFS has the strongest venue-specific Tier-A signal; TDSC, TSMC, and TCSS personal-voice samples remain too thin for strong author-by-venue claims.
- Topology-first simulation, RL/MARL/MPC, and PINN/PIDL include emerging or repository-derived capability. Do not describe them as equally mature publication-corpus directions.
- Use `references/corpus/local_corpus_metrics.json` as the quantitative source of truth and treat prose summaries as rounded interpretations.
- Use `references/FULLTEXT_CORPUS_DERIVED_DOCTRINE.md` for cross-paper model/theory/code/evidence checks and `references/corpus/open_access_fulltext_manifest.csv` for the public 31-paper expansion boundary.

## One-line signature

Write from an operational cyber/network decision problem, separate the mechanism and intervention gaps, formalize a named model/problem, derive the solution conditions, implement a verifiable solver, and close with comparative evidence and a bounded cost/timing/topology/security implication.

## Current structure

```text
Introduction
  stakes → mechanism difficulty → literature taxonomy → dual gap
  → proposed approach → model/theory/algorithm/evidence contributions

System model / problem formulation
  entities → states/units → topology → timing → actions/information
  → objective/payoff → admissibility → solution concept

Theory
  assumptions → theorem ladder → necessary/sufficient status
  → proof/dependency → numerical meaning

Algorithm
  inputs → initialization → updates → projection/reset
  → stopping residual → complexity → failure behavior

Evidence
  sanity/independent check → matched baselines
  → topology/parameter/seed coverage → sensitivity/ablation
  → uncertainty/failures → scalability → bounded implications
```

## Quantitative soft targets

- Abstract: 190–240 words, normally 8–11 sentences.
- Mean sentence length: approximately 19–26 words.
- Review sentences above 42–45 words.
- Manually inspect every sentence above 60 words.
- Contribution list: normally 2–4 items in model → theory → algorithm → evidence order.

## Preferred prose behavior

- Use active `we` for research actions.
- Name the formal object: model, problem, theorem, optimality system, algorithm, estimator, policy.
- Put the purpose or claim at the start of a paragraph.
- Use equations after the entities, units, timing, and meaning are clear.
- Narrate results as metric → magnitude/uncertainty → mechanism → bounded implication.
- Use `indicate` or `suggest` when evidence is conditional; reserve `establish` for formal or sufficiently decisive evidence.
- State the exact model, topology, parameter, information, budget, and scenario boundary.

## Phrases to use functionally, not mechanically

`However`, `To address ...`, `Based on ...`, `On this basis`, `Next`, `Furthermore`, `Finally`, `formulate`, `derive`, `establish`, `develop`, `optimality system`, `iterative algorithm`, `comparative experiments`.

Do not repeat the same connector in adjacent sentences or more than roughly three times per 500 words.

## Corrections to historical habits

Do not imitate grammar defects, vague usefulness claims, `thereby evidencing`, unsupported `first/novel/innovative`, or a claim of optimality/equilibrium based on one numerical run.

## Experiment fallback

When real propagation or attack–defense trajectories cannot be obtained:

1. acquire a semantically compatible real topology when possible;
2. call the study `real-topology simulation`, not real-world validation;
3. otherwise use a matched, multi-family synthetic topology suite;
4. generate transparent parameter, initial-state, and attack-seed scenarios;
5. verify the node-level model with an independent solver or stochastic ensemble;
6. use matched baselines, multiple graph/parameter seeds, holdouts, uncertainty, and failure logs;
7. scope every conclusion to the declared model/topology/parameter assumptions.

See `references/ATTACHMENT_CORPUS_ANALYSIS.md`, `references/FULLTEXT_CORPUS_DERIVED_DOCTRINE.md`, and `references/TOPOLOGY_FIRST_EXPERIMENT_PROTOCOL.md`.
