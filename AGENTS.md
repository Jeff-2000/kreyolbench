# AGENTS.md

## Purpose

This is the primary operating manual for Codex and any future AI coding agent working on KreyolBench.

KreyolBench is both a software project and a long-term, open-world scientific research program. Agents must optimize for scientific quality, reproducibility, extensibility, traceability, maintainability, reviewability, and future publication value while keeping every release bounded.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

Blocking downstream work:

- final v0.1 benchmark task freeze
- final annotation campaign launch
- final leaderboard ranking policy

## Mission

KreyolBench is a Kreyol-first research program and extensible benchmark ecosystem for Haitian Creole NLP and AI evaluation. It supports peer-reviewed research, open-source datasets, baseline and frontier-model evaluation, annotation campaigns, reproducible experiments, leaderboards, scientific governance, international collaboration, and public-interest Haitian Creole AI.

## Required Reading Before Editing

Before editing a subsystem, read the relevant Markdown specification:

| Subsystem | Required docs |
| --- | --- |
| Project vision/scope | `PROJECT_VISION.md`, `RESEARCH_SCOPE.md`, `ROADMAP.md`, `datasets/TASK_TAXONOMY.md` |
| Scientific governance | `SCIENTIFIC_GOVERNANCE.md`, `DECISIONS.md`, `ASSUMPTIONS.md`, `RISKS.md` |
| Data and datasets | `data/README.md`, `datasets/DATASET_SPECIFICATION.md`, `datasets/EXAMPLE_PROVENANCE.md`, `datasets/SOURCE_REGISTRY.md`, `datasets/SPLIT_POLICY.md`, `datasets/LEAKAGE_PREVENTION.md`, `datasets/VERSIONING_POLICY.md`, `reports/SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md`, `reports/source_reviews/README.md`, and the relevant `datasets/tasks/*.md` specification |
| Annotation | `annotation/README.md`, `annotation/guidelines.md`, `annotation/QUALITY_CONTROL.md`, `annotation/ADJUDICATION_PROTOCOL.md` |
| Evaluation | `eval/EVALUATION_PROTOCOL.md`, `eval/METRICS.md`, `eval/STATISTICAL_TESTING.md`, `eval/ERROR_ANALYSIS.md` |
| Baselines | `baselines/BASELINE_MATRIX.md`, `baselines/TRAINING_PROTOCOL.md`, `baselines/COMPUTE_POLICY.md` |
| Leaderboard | `leaderboard/LEADERBOARD_POLICY.md`, `leaderboard/SUBMISSION_POLICY.md`, `leaderboard/REPRODUCIBILITY_REQUIREMENTS.md` |
| Code | `src/README.md`, `tests/TEST_STRATEGY.md`, `ARCHITECTURE.md`, `REPRODUCIBILITY.md` |
| Publication and review | `PUBLICATION_STRATEGY.md`, `reports/PAPER_OUTLINE.md`, `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`, `reports/TASK_SPEC_REVIEW_PACKET_V0_1.md`, `reports/reviews/README.md`, `reports/V0_1_TASK_FEASIBILITY_MATRIX.md`, `CHANGELOG_RESEARCH.md` |

## Engineering Expectations

- Inspect before editing.
- Reuse existing abstractions when sound.
- Avoid unnecessary dependencies.
- Prefer typed Python and explicit schemas.
- Preserve backwards compatibility when reasonable.
- Add tests for code changes.
- Keep generated outputs, large data, secrets, and restricted material out of Git.
- Prefer configuration files over hard-coded scientific choices.
- Do not create fake benchmark results or pretend scaffold behavior is publication-grade.
- Do not interpret runtime task aliases, implemented validators, or any release list as the permanent KreyolBench task universe.
- Register future task families at roadmap level; do not create placeholder implementations to imply breadth.

## Scientific Expectations

- Distinguish assumptions from facts.
- Mark unsupported claims as `UNKNOWN`, `TO_VERIFY`, or `PENDING_SOURCE_REVIEW`.
- Do not invent dataset licenses, dataset sizes, model performance, annotation agreement, URLs, citations, partnerships, or publication claims.
- Treat Haitian Creole as a language with its own orthography, variation, syntax, register, and sociolinguistic context.
- Preserve raw and normalized forms when scientifically justified.
- Do not normalize linguistic diversity away merely to simplify modeling.
- Keep task family, task instance, scope status, scientific status, and release membership conceptually and mechanically separate.
- Treat first/largest/leading/best/most-comprehensive claims as unsupported until systematic comparative evidence exists.

## Human Expert Checkpoints

Engineering decisions may usually proceed without interruption when they do not alter scientific meaning.

Scientific decisions require documentation and may require `SUBMITTED_TO_REVIEW` before dependent work proceeds. Examples:

- benchmark task definition
- source inclusion/exclusion
- annotation label schema
- normalization policy
- split policy
- primary metrics
- statistical testing methodology
- leaderboard ranking policy
- publication claims
- task-family expansion and release membership

An internal or AI-assisted audit may produce a `REVISED` event but cannot satisfy an `EXTERNAL_INDEPENDENT` requirement. Task validation requires identifiable external human reviewers, affiliations, relevant expertise, conflict disclosure, dated evidence, and the qualification coverage declared in the machine-readable decision.

## Data and License Rules

- Do not download, redistribute, or commit external datasets unless source handling is documented.
- Every data source needs a source registry record.
- Raw external data belongs under ignored local paths unless redistribution is explicitly allowed.
- Human-subject, speech, consent, annotator identity, and PII-risk data require controlled access.
- Follow `DATA_ACCESS_POLICY.md`, `ETHICS_AND_DATA_GOVERNANCE.md`, and `datasets/SOURCE_REGISTRY.md`.
- Treat source-feasibility conclusions as metadata triage only. They never authorize access, collection, annotation, transformation, derived use, redistribution, scientific inclusion, or release.

## Testing Requirements

For code changes, run the relevant subset of:

- unit tests
- schema validation tests
- metric tests
- data validation tests
- leakage and split-contamination checks
- integration tests
- reproducibility checks
- `kreyolbench audit-governance --root . --format text`

If tests cannot run, state why.

## Knowledge File Rules

Knowledge files are project memory. Modify them to clarify, correct, extend, refine, or document decisions. Do not silently erase unresolved questions, risks, safeguards, or scientific scope.

Important decisions must be logged in `DECISIONS.md`. Important assumptions must be logged in `ASSUMPTIONS.md`.

## Required Status Report After Work

After each meaningful implementation step, report:

- what was implemented
- files created
- files modified
- scientific decisions made
- engineering decisions made
- open questions
- risks identified
- items requiring expert review
- current statuses
- tests or validation performed
- recommended next implementation
- suggested status for next step

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial project agent operating manual. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Added task-specification, feasibility, and example-provenance required reading. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Added open-world scope and bounded-release operating rules. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Added qualified external-review evidence rules and the internal/AI-assistance boundary. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Added mandatory reading and authorization boundaries for metadata-only source reviews. | SUBMITTED_TO_REVIEW |
