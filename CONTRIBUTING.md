# Contributing

Thank you for your interest in KreyolBench. This project welcomes researchers, engineers, linguists, statisticians, educators, Haitian Creole speakers, open-source contributors, and public-interest organizations.

Because the project handles language data, research claims, and potentially sensitive community contributions, all work follows staged access, documented review, and ethical data practices.

## Ways to Contribute

- Improve documentation.
- Review source metadata and licensing.
- Add validation tests.
- Improve preprocessing, metrics, or evaluation code.
- Add baseline models.
- Help with annotation guidelines.
- Contribute public-domain or properly licensed sources.
- Run reproducible experiments.
- Review benchmark limitations.
- Help write papers, grant drafts, or dataset cards.

## First Contribution

New collaborators start with a small, non-sensitive task. Good first tasks include:

- Review one document.
- Fix one issue.
- Annotate a tiny public sample.
- Run one public baseline.
- Write a short literature summary.
- Validate one source registry entry.

Do not request access to raw, restricted, or private data before completing an initial contribution.

## Intake and Onboarding

Collaborators may be asked to provide:

- Name, affiliation, and time zone.
- Relevant expertise.
- Desired role.
- GitHub, ORCID, Google Scholar, LinkedIn, or equivalent profile if available.
- Conflict-of-interest disclosure.
- Whether they need access to code, public data, private drafts, or restricted data.

Core collaborators may be asked to join a short onboarding call to confirm scope, expected contribution, timeline, access needs, and credit expectations.

## Development Workflow

1. Open or claim an issue.
2. Create a branch or fork.
3. Make a focused change.
4. Run relevant validation or tests.
5. Open a pull request.
6. Respond to review.

Use branch names such as:

- `docs/data-policy-update`
- `feature/asr-baseline-whisper`
- `fix/ner-schema-validation`
- `eval/xlmr-classification-baseline`

Pull requests should include:

- What changed.
- Why it changed.
- What data was used.
- What tests or validation were run.
- Any license, privacy, or ethics concerns.

## Local Checks

Install the project and run tests:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

Validate datasets before proposing dataset changes:

```bash
kreyolbench validate-dataset --task ner --path data/sample/ner.jsonl
```

## Data Contribution Rules

- Do not commit raw external data unless redistribution is explicitly allowed.
- Do not add scraped data without a source registry entry.
- Do not add private communications, private social media, or personal data.
- Do not add audio or human-subject data without documented consent and approval.
- Keep raw, clean, normalized, and annotated data separate.
- Preserve source URL, retrieval date, license, and citation metadata.

Every source must follow `docs/data_governance.md`.

## Research Contribution Rules

- Do not make claims beyond the evaluated data.
- Document limitations and known failure modes.
- Preserve failed experiments when relevant.
- Keep evaluation configs and results reproducible.
- Confirm authorship expectations before major writing or submission work.

## Conduct

All contributors must follow `CODE_OF_CONDUCT.md`. Respectful disagreement is welcome. Harassment, exploitation, plagiarism, extractive behavior, or misuse of community data is not.

