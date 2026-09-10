# Test Strategy

## Purpose

Define testing expectations for KreyolBench as both software and scientific infrastructure.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes for scientific invariants.

## Unit Tests

Cover individual utilities:

- YAML loading
- JSONL reading/writing
- hashing
- preprocessing functions
- metrics
- result serialization

## Data Validation Tests

Should check:

- valid task names
- required fields
- unique IDs
- valid splits
- valid labels
- required source metadata
- missing values
- input/target shape compatibility

## Leakage Tests

Should check:

- no duplicate IDs across splits
- no exact duplicate text across train/test unless explicitly allowed
- no near-duplicates above a defined threshold
- no hidden-test identifiers in public training artifacts

## Metric Tests

Should include:

- perfect prediction cases
- all-wrong cases
- empty input behavior
- length mismatch errors
- class imbalance behavior
- BIO boundary behavior
- retrieval qrel edge cases

## Scientific Invariants

- Raw text linkage must be preserved when normalized text exists.
- Test IDs must never occur in train.
- Source metadata must be present.
- Example provenance must identify a specific collection/subset unit and content origin.
- NER character spans may represent nesting but must not cross; nested annotation is not mandatory until reviewed.
- Retrieval qrels must resolve to existing queries and documents.
- Data with unapproved redistribution status must not appear in public release paths.
- Every non-synthetic source must have exactly one metadata-feasibility record.
- The synthetic fixture must have a separate control record and remain scientifically excluded.
- Metadata feasibility must never imply source authorization or pilot readiness.
- Source families must not be recommended directly for collection permission.

## Governance Audit Coverage

Implemented checks now cover:

- all eight project review statuses and invalid values
- required governance fields and resolvable decision IDs
- release-candidate rejection when expert decisions are unresolved
- source redistribution-state consistency
- globally unique sample IDs
- train/test exact-text contamination
- raw/normalized text linkage
- resolvable sample source IDs
- configured multi-label classification, span NER, sentiment, and code-switch labels
- decision review histories and evidence paths
- task feasibility dimensions and v0.1 coverage
- canonical retrieval corpus/query/qrel fixtures
- open-world task-family and domain registration
- stable task-instance identity and family/type resolution
- separation of scientific review status from scope status
- explicit versioned release membership
- exclusion of roadmap, discovery, feasibility-only, and deferred tasks from automatic release inclusion
- deterministic text and JSON CLI output
- source-feasibility coverage, evidence paths, and task-reference resolution
- non-authorizing feasibility conclusions and unchanged source approval gates
- synthetic-control scientific exclusion

Near-duplicate detection, document-group leakage, and release-manifest validation remain future work because their thresholds and storage contracts require scientific review.

## Acceptance Criteria

- Code changes include relevant tests.
- Release candidates pass validation.
- Publication claims are backed by reproducible testable artifacts.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial test strategy. | SUBMITTED_TO_REVIEW |
| 2026-09-08 | Added executable governance and scientific-invariant coverage. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Added task-contract, provenance, review-history, and retrieval-artifact coverage. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Added open-world taxonomy, domain, task-instance, and release-membership coverage. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Added source-feasibility coverage, evidence, family, synthetic-control, and no-authorization checks. | SUBMITTED_TO_REVIEW |
