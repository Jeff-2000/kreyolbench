# Split Policy

## Purpose

Define train, validation, public test, and hidden test split requirements.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Current Split Names

- `train`
- `validation`
- `test_public`
- `test_hidden`

## Requirements

- Splits must be frozen and hashed before release.
- Example IDs must not overlap across splits.
- Exact and near-duplicate contamination must be checked.
- Source-aware grouping should be used when documents generate multiple examples.
- Hidden tests must not be exposed before evaluation infrastructure exists.

## Open Questions

- Should split proportions vary by task?
- Should sources be held out by domain/source for domain-transfer tests?
- What near-duplicate threshold is acceptable by task?

## Acceptance Criteria

- Split generation is reproducible.
- Split hashes are stored.
- Leakage checks are documented.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial split policy. | SUBMITTED_TO_REVIEW |

