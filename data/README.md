# Data Directory

## Purpose

`data/` stores local dataset artifacts by processing stage. It is not a place to casually commit external data.

## Status

Current status: TO_REVIEW_LATER

Owner: Codex

Requires expert validation: Yes for data release decisions.

## Layout

- `raw/`: raw external data, ignored except `.gitkeep`.
- `interim/`: intermediate data, ignored except `.gitkeep`.
- `processed/`: processed release candidates, ignored except `.gitkeep`.
- `external/`: instructions or metadata for external datasets.
- `sample/`: tiny committed synthetic or public-safe fixtures for tests and examples.

## Rules

- Do not commit raw external text unless redistribution is explicitly approved.
- Do not commit restricted, private, consent, or PII-risk data.
- Keep raw text, cleaned text, normalized text, and annotations separate.
- Preserve source IDs and retrieval metadata on rows.
- Use sample fixtures only for tests and documentation, not scientific claims.

## Acceptance Criteria

- Public sample files validate against schemas.
- Release candidates have source registry coverage.
- Splits are frozen and hashed before public release.
- PII and deduplication checks are documented before release.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial data directory specification. | TO_REVIEW_LATER |

