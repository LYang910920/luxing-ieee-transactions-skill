# Deakin Academic-Resource Access Policy

## Authorized purpose

The repository owner authorizes WORK to use an **already authenticated** Deakin institutional browser session solely to locate, read, and analyze academic papers and their supplementary materials for this skill's publication-corpus audit, literature review, citation verification, and writing-style calibration.

A candidate publisher or DOI URL may be opened through:

```text
https://ezproxy.deakin.edu.au/login?qurl=<URL-encoded target URL>
```

Generate it with:

```bash
python tools/deakin_proxy_url.py "https://doi.org/10.xxxx/xxxxx"
```

## Access priority

1. lawful public/open-access full text;
2. author-accepted manuscript or institutional repository;
3. publisher full text already available to the owner;
4. Deakin EZproxy in the owner's authenticated session.

Use deliberate, paper-by-paper access. Do not bulk scrape or attempt to defeat publisher rate limits.

## Prohibited actions

WORK must not:

- request, view, copy, infer, export, or disclose passwords;
- access or manipulate cookies, session tokens, local storage, autofill, password managers, browser history, or account settings;
- bypass MFA, DUO, paywalls, download limits, robots controls, or any access restriction;
- submit forms, purchase content, accept paid terms, send email, or modify library/account records;
- collect unrelated personal data;
- redistribute publisher PDFs, supplementary files, or substantial copyrighted text;
- commit institutional downloads to Git or include them in a release ZIP.

If authentication or MFA is required, pause and ask the owner to complete it personally.

## Permitted retained data

The project may retain:

- bibliographic metadata, DOI, venue, year, authorship role and access route;
- derived section maps, sentence/paragraph statistics, phrase frequencies, rhetorical-move labels and brief paraphrased notes;
- research-method, theorem, algorithm, experiment and limitation summaries;
- short quotations only when necessary and legally permitted;
- owner-only PDFs under `corpus/private/`, subject to licence terms and excluded from Git/release archives.

## Required audit fields

For every candidate paper update at least:

```text
fulltext_checked
access_route
access_date
source_url_or_doi
role_confidence
style_eligible
paper_card
closest_overlap
novelty_impact
must_cite
notes
```

Any paper that weakens a novelty claim must be recorded prominently, not hidden.
