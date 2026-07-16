# Corpus Provenance

## Current sources

The seed package was assembled from:

- the owner's current CV and publication/contribution records;
- article full texts already available in the owner's file collection, including files accessed under Deakin's institutional licence;
- Deakin Experts, Google Scholar, ORCID and DBLP as bibliographic entry points;
- publisher/DOI metadata for selected papers;
- the owner's public Git repositories as evidence of preferred reproducibility and repository organization.

The v0.4.0 research-doctrine expansion contains 73 verified full texts: 42 owner-provided papers and 31 nonduplicate open-access journal articles associated with ORCID `0000-0002-9229-5787`. Open-access inclusion required actual PDF bytes or complete publisher HTML rather than an abstract or metadata record. The discovery set is documented in `corpus/open_access_fulltext_manifest.csv`.

This is an expanded partial calibration, not a complete-publication claim. Bibliographic discovery can miss records, and lawful full text was not verified for every discovered article.

## Provenance classes

| Class | Meaning | May influence style? |
|---|---|---|
| A | First author plus documented conceptual/manuscript leadership | Strongly |
| B | Corresponding author plus documented conceptual/writing/revision leadership | Strongly, especially for current evolution |
| C | Coauthor with documented substantial writing | Moderately |
| D | Coauthor role unclear | Weakly; architecture only unless corroborated |
| E | Editorially transformed proof, review, lecture, proposal or non-paper genre | Exclude or isolate |

The 31 open-access additions default to research-architecture and correction evidence unless a separate authorship-role audit justifies sentence-level use. They strengthen mechanism, theorem, solver, baseline, leakage, and claim-language gates without changing the attachment-derived sentence metrics.

## Version handling

Prefer the accepted/final article for public section architecture and the author's submitted/accepted manuscript for personal voice when both are legally available. Record both and compare editorial changes. Do not count duplicate downloads or preprint/final versions as separate style samples.

## Copyright boundary

Full texts and per-paper deep-reading notes remain workspace/private inputs even when the source article is open access. Public repository artifacts contain only lawful bibliographic metadata, aggregate counts, derived rules, paraphrased summaries, and short common phrases. `corpus/private/`, PDFs, extracted text, figures, tables, and source equations are excluded from Git and release archives.
