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
- Data with unapproved redistribution status must not appear in public release paths.

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
- configured classification, sentiment, NER, and code-switch labels
- deterministic text and JSON CLI output

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
