# Git Publication Checklist

## Proposed repository

```text
name: luxing-ieee-transactions-skill
description: Evidence-gated IEEE Transactions research and writing skill with Lu-Xing Yang style calibration, topology-first node-level experiments, synthetic/real-data evidence contracts, and three-repository method integration.
topics:
  - ieee
  - academic-writing
  - research-workflow
  - cybersecurity
  - network-topology
  - node-level-models
  - optimal-control
  - differential-games
  - reinforcement-learning
  - physics-informed-learning
  - simulation
  - reproducibility
  - agent-skill
```

## Before first public push

- [ ] Owner explicitly authorizes publication.
- [ ] Repository name and MIT licence for this SKILL are confirmed.
- [ ] `CITATION.cff` repository URL/DOI is added when available.
- [ ] Version and release status agree across the READMEs, style profile, `project_manifest.json` and runtime `__version__`; any optional `VERSION`, `pyproject.toml` or `CITATION.cff` added later agrees too.
- [ ] No upstream `academic-research-skills` text is copied.
- [ ] No nested copy of any of the three tutorial repositories exists.
- [ ] Foundation no-blanket-licence boundary has been reviewed and respected.
- [ ] Note 1/Note 2 path-specific licence notices have been reviewed.
- [ ] Repository snapshot commits and retrieval dates have been refreshed.
- [ ] No publisher PDF, owner paper archive, extracted article text, supplementary ZIP, review file or accepted manuscript is included.
- [ ] No `private/`, `raw/` or checkpoint directory is present in the tracked tree or release.
- [ ] `corpus/local_attachment_manifest.csv` contains only bibliographic/derived fields and hashes, not article text.
- [ ] `corpus/open_access_fulltext_manifest.csv` contains only public bibliographic/provenance fields, not downloaded files or extracted text.
- [ ] Per-paper deep-reading notes, figure crops, evidence bundles and raw full text remain outside the release.
- [ ] All attachment paper cards are paraphrased summaries with no long quotation, copied table, equation or figure.
- [ ] The release status is not `full-corpus-calibrated` unless the full-corpus audit has actually passed.
- [ ] No raw graph/dataset, PCAP, malware sample, checkpoint, testbed log or private telemetry is included.
- [ ] Topology and dataset candidate references do not imply a licence grant, privacy clearance or redistribution right.
- [ ] Generated graph examples contain no accidentally retained real node labels, account identifiers or sensitive attributes.
- [ ] No institutional download footer or `Authorized licensed use` text appears in tracked files.
- [ ] No credentials, cookies, tokens, browser profiles, absolute private paths or user-specific cache paths are present.
- [ ] All temporally unstable metadata is dated or omitted.
- [ ] `python -m unittest discover -s tests -v` passes.
- [ ] `python scripts/luxing_ieee.py validate` passes.
- [ ] `python scripts/validate_skill.py --json` returns `ok: true`.
- [ ] The system `skill-creator/scripts/quick_validate.py` passes against the repository root.
- [ ] `analyze-local-corpus` has been checked for derived-only output; `recommend-topology`, `audit-topology` and `audit-evidence` smoke examples pass.
- [ ] Release ZIP listing and its generated `<archive>.sha256` file have been independently inspected.
- [ ] Extracted release has been re-tested, not only the working tree.

## Suggested first commits

```text
chore: initialize personalized IEEE Transactions skill
feat: add owner key-paper corpus metrics and style tiers
feat: add corpus verification and Deakin-safe gap filling
feat: integrate three repository research layers
feat: add topology-first and synthetic simulation evidence contracts
feat: add data adapters claim gates and project scaffolding
feat: add metrics linter audits and tests
docs: add release provenance licence and publication notes
```

## Suggested v0.4.0 release note

This `expanded-partial-calibration` release provides an executable IEEE Transactions research-and-writing workflow informed by 73 verified full-text deep readings: 42 owner-provided papers and 31 nonduplicate open-access journal articles. The expanded corpus adds cross-paper mechanism, state/unit, theorem/dependency, delay/fractional/impulse, Hamiltonian/solver, baseline/probability, leakage, and text–figure consistency gates. Sentence-level personal-style metrics remain anchored to the role-weighted 42-paper local corpus, including 20 first/corresponding-author core-voice papers and 17 IEEE Transactions full texts. The release distributes only lawful bibliographic metadata, aggregate counts, derived rules and metrics, checksums, and paraphrased paper cards. It does not claim a verified complete publication universe and bundles no PDF, extracted text, per-paper reading note, tutorial source, graph dataset, or third-party data.

## Public/private split option

Keep the SKILL repository public and use separate private locations for:

- `LYANG PAPER.zip`, licensed article full text and acquisition logs;
- extracted article text and parser-debug output;
- raw or restricted graph/dataset files;
- packet captures and malware samples;
- checkpoints, testbed configuration and logs;
- manuscript and reviewer-confidential materials.

Export only reviewed derived paper cards, corpus aggregates, dataset/topology metadata, model mappings and non-sensitive artefacts to the public repository.
