# Full-Corpus Style Audit Protocol

## Goal

Produce a reproducible, role-aware and time-aware profile of Lu-Xing Yang's IEEE Transactions research writing without redistributing article text or over-attributing collaborator prose.

Version 0.4.0 starts from an expanded verified-full-text working corpus: 42 owner-provided papers plus 31 nonduplicate open-access journal articles, for 73 paper-by-paper deep readings. The local subset contains 20 first/corresponding-author core-voice papers and 17 IEEE Transactions papers. All 17 owner-priority selected Transactions rows have private full text; one different-subfield row is owner-deprioritized. This is substantial research-doctrine calibration evidence, but it is not automatically the complete publication universe or sentence-level voice evidence.

## 1. Establish the publication universe

Build a superset from:

- the owner-provided local archive;
- Deakin Experts;
- Google Scholar as a discovery index, not the sole source of truth;
- ORCID;
- DBLP;
- DOI/Crossref and publisher metadata;
- the current CV and owner records.

Deduplicate by normalized DOI when available; otherwise use normalized title, year and author sequence. Record online-first versus issue dates, conference/journal relationships, accepted-manuscript/publisher versions, corrections, errata and title variants.

## 2. Use local full text as the first fallback

When the owner supplies a local archive such as `LYANG PAPER.zip`:

1. inspect the archive listing before extraction;
2. reject path traversal, executables and unexpected nested archives;
3. extract only to `corpus/private/local_fulltext/` or an external private workspace;
4. run `verify-local-corpus` against `corpus/local_attachment_manifest.csv`;
5. run `analyze-local-corpus` to reproduce derived-only abstract/prose metrics;
6. investigate every missing, unexpected, duplicate, checksum-mismatched or materially drifting file;
7. do not commit PDFs, extracted text, figures, tables, equations or publisher files;
8. export only reviewed metadata, aggregate metrics and paraphrased paper cards.

A local attachment should be preferred over a new publisher download when it is the same lawful version and has adequate text quality. Deakin access is a gap-filling route, not a requirement to re-download content already supplied by the owner.

## 3. Determine style eligibility

Include sentence-level style evidence only when:

- the paper is an English research article;
- a usable full text is lawfully available;
- the owner's writing/conceptual role is known or can be bounded;
- editorial transformations do not make attribution unusable.

Assign one of these tiers:

```text
A_core_voice
  first author, corresponding author, or documented original-draft responsibility

B_editorial_influence
  documented review/editing contribution without clear original-draft ownership

C_research_architecture_only
  coauthored without writing-role evidence, or documented nonwriting contribution
```

Tier C can inform research architecture, method combinations and experiment evolution, but must not dominate vocabulary or sentence-rhythm rules. Mark uncertainty rather than silently treating every coauthored sentence as personal voice.

## 4. Segment by rhetorical function

Extract or map, at minimum:

```text
abstract
introduction
related work/background
model/problem formulation
theory/proofs
algorithm
experimental setup
results/discussion
limitations/future work
conclusion
```

A paper may combine headings. Map functions rather than relying only on section labels. Two-column PDF extraction can corrupt paragraph boundaries, so report paragraph metrics only when layout confidence is adequate.

## 5. Compute quantitative features

Per section and paper, where extraction quality permits:

- word, sentence and paragraph counts;
- sentence mean, median, standard deviation, p90 and maximum;
- proportions of short (≤14), medium (15–30), long (31–45) and very long (>45) sentences;
- paragraph function and, when reliable, paragraph-length distribution;
- first-person research-action frequency;
- transition, hedge, reporting-verb and action-verb counts per 1,000 words;
- citation markers and approximate citation density;
- figure/table/equation/theorem references;
- claim-strength vocabulary;
- repeated three- to five-word n-grams after removing equations and references.

Do not treat equation tokens, headers, footers or reference lists as prose. Keep a parser/version record so metric changes can be reproduced.

## 6. Annotate rhetorical moves

Use `RHETORICAL_MOVE_MAP.md`. Record move order and omissions for:

- abstracts;
- Introduction problem/gap/proposal/contribution flow;
- contribution lists;
- theorem-to-algorithm bridges;
- experiment setup and result paragraphs;
- conclusions and limitations.

Distinguish a stable author signature from a venue template or collaborator-specific structure.

## 7. Attribute voice and weight evidence

Assign role confidence using contribution statements, author position, corresponding status, drafts/revisions and owner confirmation. Apply the weights in `profiles/lu_xing_yang_current.yaml`.

Where a section is known to have been written by a collaborator, exclude it from sentence-level calibration or tag it separately. Do not infer writing ownership solely from corresponding status.

## 8. Model time evolution

Use at least these periods:

```text
early/foundational: through 2018
decision-problem/optimality phase: 2019–2023
current explicit-gap/layered-validation phase: 2024–present
```

Compare architecture, sentence metrics, claim language, evaluation design and limitations. Separate genuine evolution from venue, article type and coauthor effects.

## 9. Synthesize four layers

### Stable signature

Traits supported across periods, venues and high-confidence samples.

### Current evolution

Traits concentrated in recent high-confidence papers and consistent with the owner's current research workflow.

### Venue-specific overlays

Traits required by the current target journal rather than by the author's general style.

### Legacy artifacts to correct

Grammar errors, vague promotional language, repeated connectors, weak validation or outdated conventions that should not be imitated.

## 10. Report uncertainty and coverage

For every profile field assign high, moderate or low confidence. Report:

- owner-provided paper count;
- publication-universe count and reconciliation date;
- full-text coverage overall and for selected Transactions papers;
- high-confidence authorship coverage;
- year and venue distribution;
- sections analyzed and extraction quality;
- inaccessible/blocked items;
- duplicate/version decisions;
- likely collaborator/editor effects.

The current v0.4.0 baseline should be reproducible as:

```text
42 owner-provided readable full texts
31 nonduplicate open-access full texts verified to PDF or complete publisher HTML
73 paper-by-paper deep-reading notes with final evidence/lint gates
20 first/corresponding core-voice papers
17 IEEE Transactions full texts
17/18 selected Transactions rows covered by private full text
17/17 owner-priority selected rows covered; 1 row owner-deprioritized
```

Any difference must be explained rather than silently overwritten.

## 11. Completion statuses

Use the most accurate status:

```text
attachment-key-corpus-calibrated
  owner key-paper corpus analyzed, but publication universe not yet proven complete

expanded-partial-calibration
  additional lawfully acquired papers analyzed, but coverage or role evidence remains incomplete

full-corpus-calibrated
  publication universe reconciled, required coverage met, duplicates resolved,
  role uncertainty documented and quality gates passed
```

`full-corpus-calibrated` requires the quantitative and provenance criteria in this protocol. A large or deeply read working corpus alone is not sufficient if the publication universe, missing papers, duplicates, versions, and role evidence have not been reconciled.
