# Local Full-Text Fallback Protocol

## Purpose

Use owner-provided full text before institutional retrieval whenever available. The local attachment corpus is both safer and more reproducible than repeatedly depending on publisher access, while Deakin and public sources remain necessary for missing papers, version checks, corrections, or a complete publication inventory.

## Source priority

For every candidate paper, use:

1. owner-provided PDF or source manuscript;
2. official open-access or author-posted version;
3. institutional repository;
4. licensed publisher access through an already authenticated Deakin session.

Do not re-download a paper solely because a publisher version exists when the owner-provided file is sufficient for structure and prose analysis. Record version differences when pagination, title, author order, or text differs materially.

## Private storage

The working full texts belong under:

```text
corpus/private/local_fulltext/
```

The directory must remain ignored by Git and excluded by the release builder. Do not put extracted article text, page images, publisher figures, or long quotations into tracked files.

Tracked outputs may include only:

- bibliographic metadata;
- file checksum;
- page count;
- authorship/contribution classification;
- aggregate metrics;
- short phrase counts;
- section/move labels;
- derived paper cards;
- uncertainty and conflict notes.

## Attachment verification

The v0.4.0 release preserves `corpus/local_attachment_manifest.csv` as the sentence-style source manifest. WORK should:

1. place the 42 owner PDFs in the private directory;
2. run `python -m luxing_ieee_skill verify-local-corpus corpus/private/local_fulltext`;
3. run `python -m luxing_ieee_skill analyze-local-corpus corpus/private/local_fulltext --report reports/local_corpus_reanalysis.json`;
4. investigate missing, duplicate, or checksum-mismatched files;
5. record whether a mismatch is a benign alternate version or a provenance problem;
6. never overwrite the tracked manifest silently.

A checksum mismatch does not prove tampering; publisher and author-manuscript versions can legitimately differ. It requires manual version resolution.

## Attribution gate

Before using a paper for sentence-level calibration, classify it:

```text
A_core_voice
B_editorial_influence
C_research_architecture_only
```

Use contribution statements where available. First/corresponding position is evidence, not certainty. A coauthored paper with unclear writing responsibility should not dominate lexical preferences.

## Deakin use after the attachment

Use Deakin or public indexing to:

- retrieve a selected Transactions full text only if the owner reactivates the currently deprioritized row;
- verify the publisher-final status, DOI, pagination, appendices, and version relationship of the 2026 TDSC-matched author manuscript;
- verify whether later corrections or final versions exist;
- identify key publications absent from the attachment;
- resolve title/DOI/online-first conflicts;
- confirm corresponding-author and contribution records.

Follow `DEAKIN_ACCESS_POLICY.md`. Do not inspect cookies, tokens, passwords, local storage, browser history, or unrelated account data. Pause for owner-controlled MFA.

## Completion language

Allowed:

- `attachment-key-corpus-calibrated`;
- `expanded-partial-calibration` when the separate 31-paper open-access manifest and 73-note inventory audit pass;
- `42 owner-provided full texts analyzed`;
- `17/18 selected Transactions rows covered by private full text`;
- `17/17 owner-priority selected Transactions rows covered; one row owner-deprioritized`.

Not allowed until independently verified:

- `all publications analyzed`;
- `complete author corpus`;
- `full-corpus-calibrated`;
- `all papers downloaded from Deakin`.
