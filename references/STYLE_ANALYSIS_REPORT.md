# Style Analysis Report

## Decision

The overall profile is now **expanded-partial-calibration**. Sentence-level style remains calibrated from 42 owner-provided full-text papers, including 17 IEEE Transactions papers and a 20-paper first/corresponding-author core-voice subset. A separate 31-paper open-access expansion brings the research-doctrine corpus to 73 full-text deep readings; it strengthens architecture and correction rules without altering the personal-voice core or local sentence metrics.

It is not yet a complete-publication-corpus claim. All 17 owner-priority selected Transactions rows now have private full text; the only uncovered row is an explicitly owner-deprioritized different-subfield paper. The broader publication universe, authorship roles, and version conflicts still require reconciliation.

Detailed evidence: `references/ATTACHMENT_CORPUS_ANALYSIS.md`  
Machine-readable metrics: `corpus/local_corpus_metrics.json`  
Paper-level records: `corpus/local_attachment_manifest.csv`

## Corpus methodology

1. Extract text locally from each owner-provided PDF without OCR.
2. Correct title, venue, year, DOI, author position, and corresponding-author signals where the PDF supplied them.
3. Detect abstract moves and major section categories.
4. Compute abstract sentence and word statistics.
5. classify methods, evidence types, and explicit Introduction features.
6. weight sentence-level style by authorship and contribution evidence.
7. retain only derived measurements and paper cards in the release.

The PDF layout can affect paragraph boundaries and a small number of abstract counts. Accordingly, the profile uses ranges and document frequencies rather than pretending the extraction is typographically exact.

## Coverage

- 42 full texts, 2012–2026;
- 15 first-author papers;
- 9 papers with the owner identified as corresponding author;
- 20 distinct first/corresponding-author core-voice papers;
- 17 IEEE Transactions papers;
- 19 papers from 2024 onward;
- 17 of 18 selected Transactions manifest rows covered by private full text;
- 17 of 17 owner-priority selected Transactions rows covered, with one row explicitly deprioritized.

## Current writing signature

The current refined manuscript should normally move through:

```text
operational problem and stakes
→ mechanism/representation gap
→ intervention/strategy gap
→ named model/framework/problem
→ control, optimization, game, or learning formulation
→ theorem/necessary conditions/optimality system
→ algorithm, solver, or estimator
→ comparative and stress-tested evidence
→ cost, timing, scalability, topology, or security implication
```

The repeated logic is **problem → formal object → verified computation → decision insight**.

## Abstract profile

Derived soft target:

- 190–240 words;
- 8–11 sentences;
- mean sentence length about 19–26 words;
- one operational context sentence;
- one precise gap/unresolved-decision sentence;
- model/framework and decision-problem sentences;
- theory and algorithm only when they are real contributions;
- one evaluation sentence with setting/baselines;
- one quantified or otherwise evidence-bounded finding;
- one implication sentence.

The IEEE Transactions subset is denser than the early corpus: approximately 224 weighted abstract words and 23.1 words per sentence. Recent papers average roughly 232 words and 10.4 sentences, compared with about 151 words and 7.8 sentences in the 2012–2018 subset.

## Introduction profile

The dominant current pattern is:

1. threat/system context and affected decision maker;
2. why topology, strategic interaction, timing, human behavior, information, or constraints make the problem hard;
3. related-work families;
4. exact limitation after each family;
5. consolidated dual gap;
6. proposed approach and fit to the gap;
7. 2–4 contributions ordered as model/problem → theory → algorithm → evidence;
8. organization paragraph only when useful.

A gap paragraph should not rely on `few studies`, `has not been considered`, or `to the best of our knowledge` without a logged full-text novelty audit.

## Model and theory profile

The corpus repeatedly benefits from:

- explicit state/entity definitions;
- topology or mixing assumptions;
- control and action timing;
- objective/payoff and resource cost;
- solution concept;
- theorem or necessary conditions;
- forward–backward or iterative numerical solution.

The current skill strengthens this by requiring units, information patterns, necessary-versus-sufficient status, theorem-to-code mapping, residual checks, and counterexample/edge-case search.

## Algorithm profile

A publishable algorithm section must state:

- input model and resolved parameters;
- initialization;
- update order;
- projections, bounds, impulses, or reset maps;
- stopping criterion and residual;
- convergence evidence;
- complexity and resource use;
- failure behavior and retained failed runs.

A decrease in objective or training loss alone is not stationarity, equilibrium, identifiability, or convergence proof.

## Experiment profile

The older corpus is mainly model/theory/numerical. The current profile expands this into an evidence ladder:

- deterministic numerical verification;
- stochastic/agent-based/closed-loop simulation;
- real-topology or trace-driven simulation;
- real-observation calibration and held-out prediction;
- testbed/emulation/field evidence when required.

When real propagation data are unavailable, the preferred fallback is:

```text
semantically valid observed topology
+ transparent synthetic dynamics/parameters
+ node-level numerical or stochastic simulation
+ matched synthetic graph controls
+ graph/parameter/attack-seed repetitions
+ independent validation
+ scoped claim language
```

## Lexical habits

Frequent short functions across the 42 abstracts include:

- `First`, `Second`, `Next`, `Finally`;
- `Based on`, `On this basis`;
- `To address`, `However`;
- `formulate`, `derive`, `establish`, `develop`, `propose`;
- `optimality system`, `iterative algorithm`, `Nash equilibrium`;
- `comparative experiments`, `numerical experiments`;
- `cost-effective`.

Use these selectively. They should organize reasoning, not serve as stylistic decoration.

## Titles

The corpus often combines the problem with the method or solution notion. Common forms include gerund-led titles, colon-separated problem/method titles, and terms such as model, approach, strategy, policy, or cost-effective.

A title must remain evidence-bounded. `Optimal`, `robust`, `scalable`, `practical`, and `real-world` are gated terms.

## Legacy corrections

Do not reproduce:

- subject–verb disagreement;
- `presents challenging`;
- `thereby evidencing`;
- vague “would be helpful” endings;
- repeated `On this basis`;
- unsupported superlatives;
- one-sentence combinations of novelty, model, algorithm, results, and implication;
- equilibrium/optimality claims based only on one converged numerical trace.

## Confidence

High confidence:

- macro structure;
- abstract move order;
- contribution order;
- problem-first Introduction;
- formal-then-computational architecture;
- current movement toward related-work taxonomies, explicit gaps, named objects, layered experiments, and limitations.

Moderate confidence:

- precise phrase preferences;
- title habits;
- sentence ranges by section.

Pending:

- definitive citation-integration ratio;
- complete publication coverage;
- collaborator-specific prose separation;
- venue-specific style beyond the five journal overlays.

## Consumption rule

The profile is a soft guide. The priority order is:

```text
truth/evidence/ethics
> current journal and discipline conventions
> frozen project and reproducibility contract
> current author profile
> historical phrasing
```
