# Attachment Key-Paper Corpus Analysis

## Status and purpose

The local sentence-style component uses the owner-provided `LYANG PAPER.zip` plus two separately supplied papers as a full-text fallback corpus. The private input contains **42 readable article PDFs covering 2012–2026**. All 42 yielded usable text without OCR. Version 0.4.0 keeps these local metrics stable while adding a separate 31-paper open-access research-doctrine expansion. The release package contains only derived metadata, counts, paper cards, and checksums; it does **not** contain PDFs, extracted article text, figures, tables, equations, or long quotations.

The two additions have different provenance. The 2023 TIFS APT paper is a licensed IEEE publisher Version of Record. The 2026 TDSC-matched employee-compliance paper is an author-generated IEEE-class manuscript without publisher metadata, final pagination, DOI, or included appendices. Both are retained as Tier C research-architecture evidence because the owner is third author and no personal writing-role evidence was found.

This corpus substantially improves the writing profile when publisher or Deakin full text is unavailable. It is still described as a **key-paper corpus**, not a verified complete publication universe.

## Corpus coverage

| View | Count |
|---|---:|
| Owner-provided full-text papers analyzed | 42 |
| First-author papers | 15 |
| Papers with the owner identified as corresponding author | 9 |
| Distinct first- or corresponding-author core-voice papers | 20 |
| IEEE Transactions papers | 17 |
| All IEEE venues | 20 |
| Papers from 2024 onward | 19 |
| Selected Transactions manifest rows with private full text | 17 of 18 (94.44%) |
| Owner-priority selected Transactions rows with private full text | 17 of 17 (100%) |
| Owner-deprioritized different-subfield rows | 1 |

No owner-priority row remains without private full text. The one uncovered selected row is the owner-deprioritized PCA face-recognition paper and is retained only as an inventory item. This closes the current priority-set gap, not the broader publication-universe audit. The package must not call itself `full-corpus-calibrated` until the publication universe, duplicates, authorship roles, and version conflicts have been reconciled.

## Attribution-aware weighting

Coauthored papers are not treated as equally diagnostic of sentence-level personal style.

- **Tier A — core voice:** first-author, corresponding-author, or documented original-draft responsibility. These papers drive lexical, sentence-rhythm, abstract, and paragraph-level guidance.
- **Tier B — editorial influence:** documented review/editing contribution without clear original-draft ownership. These papers provide secondary evidence of current preferences.
- **Tier C — research architecture only:** coauthored papers without writing-role evidence, or with explicitly nonwriting contributions. These papers inform topic evolution, method combinations, experiment design, and contribution architecture, but do not override Tier A prose patterns.

The machine-readable record is `corpus/local_attachment_manifest.csv`; each paper has a derived card under `corpus/attachment_paper_cards/`.

## Quantitative profile

The measurements below are deterministic PDF-text estimates and should be interpreted as ranges rather than typographic ground truth.

| Subset | Papers | Weighted abstract words | Weighted sentences | Mean words/sentence | Median longest sentence |
|---|---:|---:|---:|---:|---:|
| All attachment papers | 42 | 200.0 | 9.4 | 21.4 | 34.0 |
| Core voice: first or corresponding | 20 | 197.7 | 9.1 | 21.9 | 38.5 |
| IEEE Transactions | 17 | 224.3 | 9.9 | 23.1 | 42.0 |
| Recent, 2024–2026 | 19 | 231.6 | 10.4 | 22.7 | 39.0 |
| Early, 2012–2018 | 12 | 151.4 | 7.8 | 19.5 | 33.0 |

### Refined drafting targets

These are soft targets; the target journal's current author instructions always win.

- Abstract: normally **190–240 words**, approximately **8–11 sentences**.
- Sentence rhythm: technical sentences commonly fall near **19–26 words**, with shorter transition/conclusion sentences mixed in.
- Review sentences above roughly **42–45 words** for unnecessary clause stacking.
- Treat sentences above **60 words** as mandatory manual-review candidates.
- Preserve density, but split a sentence when it contains more than one independent contribution, result, or qualification.

## Stable rhetorical signature

The dominant research arc across the corpus is:

```text
operational cyber/network/social problem
→ mechanism or representation gap
→ intervention, control, or strategic-decision gap
→ named model/framework/problem
→ optimal control, impulse control, differential game, or learning formulation
→ necessary conditions/theorem/optimality system
→ iterative or numerical solver
→ comparative experiments
→ cost, timing, scalability, or policy/security insight
```

The most distinctive feature is not a particular word. It is the closed transition from a real decision problem to a formal object and then back to an actionable, evidence-bounded interpretation.

## Evolution across the corpus

### 2012–2018: model and dynamical-property led

The early structure is usually:

```text
problem context
→ new propagation model
→ threshold/stability or persistence analysis
→ numerical examples
→ concise discussion/conclusion
```

Abstracts are shorter, explicit contribution headings are rare, and the prose often relies on passive constructions or theorem-led sequencing. These papers remain useful for mathematical exposition but should not dictate current Introduction architecture.

### 2019–2023: decision problem and optimality system

The middle period more often follows:

```text
security/social objective
→ control or game problem
→ necessary conditions / optimality system
→ iterative numerical algorithm
→ comparative strategy experiments
```

The paper object becomes more explicit: a named problem, solution concept, candidate strategy profile, and numerical procedure.

### 2024–2026: explicit gap synthesis and layered validation

Recent papers show a stronger journal-facing pattern:

```text
motivation and threat context
→ related-work taxonomy
→ consolidated modeling and strategy gaps
→ named framework/model/problem/algorithm
→ theory and solver
→ real or synthetic network experiments
→ convergence/scalability/robustness/limitations
```

In the 19 recent papers, explicit contribution and related-work sections are common; problem statements, novelty subsections, motivation subsections, and limitations/future-work sections appear much more often than in the early corpus. The added employee-compliance manuscript also strengthens a current research-architecture signal: hierarchical incentives, human compliance decisions, node-level intranet risk, and bilevel numerical solution are treated as one coupled decision problem.

## Abstract move pattern

The preferred current abstract is a compact research pipeline rather than a generic summary:

1. establish the operational stakes;
2. identify a precise limitation or unresolved decision;
3. introduce the model or framework;
4. formulate the control, optimization, or game problem;
5. state the theoretical characterization;
6. name the numerical/learning algorithm when it is a contribution;
7. specify the evaluation environment and strongest comparison;
8. close with one bounded practical or strategic implication.

Do not force all eight moves when the article type or journal limit does not support them. In particular, do not invent a theoretical contribution or real-data claim merely to mimic the pattern.

## Introduction architecture

A current-style Introduction should normally perform these functions:

```text
P1: threat/system stakes and affected decision maker
P2: mechanism, topology, behavior, or information difficulty
P3–P5: closest literature families, each followed by its exact limitation
P6: consolidated modeling gap + intervention/solution gap
P7: proposed approach and why it fits the gap
P8: 2–4 contribution items in model → theory → algorithm → evidence order
P9: paper organization, only when the journal/length warrants it
```

A strong contribution list names the scientific object rather than only the activity:

- model/framework/problem;
- theorem, necessary conditions, or solution characterization;
- algorithm, solver, or estimator;
- comparative, robustness, scalability, real-topology, or predictive evidence.

Avoid contribution bullets that merely say “we conduct extensive experiments” or repeat the abstract.

## Section-level register

Derived sentence metrics support a meaningful register shift:

- **Model:** definition-first and comparatively lean.
- **Problem formulation:** precise about admissible decisions, bounds, objective, information, and solution concept.
- **Theory:** dependency-aware, with necessary/sufficient status stated explicitly.
- **Algorithm:** procedural and reproducible; define stopping rules and residuals.
- **Experiments:** observation first, mechanism second, bounded implication third.
- **Discussion/limitations:** more interpretive but less absolute.
- **Conclusion:** synthesize the closed contribution chain and state exact limitations.

## Preferred lexical functions

Short recurrent phrases found across the abstracts include:

- sequencing: `First`, `Second`, `Next`, `Finally`;
- derivation bridge: `Based on ...`, `On this basis`;
- problem response: `To address ...`, `However`;
- research actions: `formulate`, `derive`, `establish`, `develop`, `propose`;
- formal objects: `optimality system`, `iterative algorithm`, `Nash equilibrium`;
- evaluation labels: `comparative experiments`, `numerical experiments`;
- objective framing: `cost-effective`.

These are **functions**, not mandatory strings. Repetition limits apply. A draft should not use `On this basis`, `Based on`, or `Finally` mechanically in every section.

## Title habits

Across the 42-paper attachment corpus:

- 14 titles use a colon;
- 10 are gerund-led, such as “Mitigating” or “Modeling”;
- 10 emphasize effective, effectiveness, or cost-effectiveness;
- 12 use “approach”;
- 13 use model/modeling;
- 11 use strategy, policy, or scheme.

The preferred title pattern is:

```text
decision/security problem + mechanism or objective
[: method or solution notion]
```

A title should not claim “optimal,” “practical,” “robust,” or “real-world” unless the paper's evidence supports the adjective.

## Result narration pattern

A result paragraph should normally follow:

```text
reference the figure/table and comparison
→ report the measured change with unit and uncertainty
→ explain the mechanism, control allocation, topology, or information reason
→ state the implication within the tested range
```

Avoid replacing measurement with adjectives such as “remarkable,” “superior,” or “significant.” When statistical significance is not tested, report magnitude, variation, and scenario coverage instead.

## Legacy artifacts to correct, not imitate

The attachment confirms that some historical English forms should be treated as editing targets rather than personal style:

- subject–verb disagreement;
- `presents challenging`;
- `thereby evidencing`;
- vague utility claims such as “would be helpful”;
- overlong sentences that combine novelty, method, result, and implication;
- unsupported `first`, `novel`, `innovative`, `superior`, `significant`, `practical`, or `optimal balance`;
- declaring an equilibrium or optimum from a single converged run.

The current refined style keeps the problem-first architecture and formal-to-computational progression while using cleaner syntax and stronger evidence gates.

## Confidence boundaries

High confidence:

- macro research arc;
- abstract move order;
- model → theory → algorithm → evidence contribution order;
- problem-first Introduction;
- derive-then-compute structure;
- active research verbs and bounded result interpretation;
- evolution toward explicit related work, contributions, and limitations.

Moderate confidence:

- precise phrase preferences;
- sentence-length range by section;
- title habits.

Not yet definitive:

- author-specific citation integration ratio;
- paragraph-length distribution, because PDF extraction can merge columns and paragraphs;
- collaborator-specific sentence patterns;
- a complete venue-by-venue style profile;
- global full-publication coverage.

The complete derived measurements are in `corpus/local_corpus_metrics.json`.
