# Scripts

## Purpose

`scripts/` contains command wrappers and project operations that should remain reproducible and auditable.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: No unless scripts change scientific meaning.

## Rules

- Prefer CLI entry points in `src/kreyolbench/cli.py`.
- Scripts should be thin wrappers, not hidden business logic.
- Scripts must not download or redistribute external datasets without source review.
- Scripts that generate release artifacts must record inputs, configs, and versions.

## Acceptance Criteria

- Script purpose is documented.
- Script output locations are ignored or release-approved.
- Script behavior is testable or manually validated.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial scripts specification. | TO_REVIEW_LATER |

