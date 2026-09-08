# Source Registry

## Purpose

Define required source metadata and review gates.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Codex

Requires expert validation: Yes

## Required Fields

Each source registry record must track:

- `source_id`
- `name`
- `url`
- `provider`
- `language_claim`
- `domain`
- `data_type`
- `license`
- `redistribution_allowed`
- `commercial_use_allowed`
- `access_method`
- `expected_tasks`
- `quality_notes`
- `privacy_risk`
- `status`
- `review_status`

The configuration field corresponding to privacy risk is currently `pii_risk`. A future schema migration may rename it only through a documented compatibility decision.

## Review Status Values

- `pending_legal_review`
- `pending_subset_review`
- `reviewed_public_domain_notice`
- `reviewed_standard_wikimedia_terms`
- `not_approved_for_redistribution`
- `approved_link_only`
- `approved_derived_only`
- `approved_public_release`

Project lifecycle `status` uses the uppercase review-status system. Source-specific `review_status` uses the values above and describes legal/data handling, not scientific suitability.

## Rules

- External datasets should usually be referenced through source URLs and reproducible acquisition logic.
- Do not download or redistribute a dataset unless legal and technical handling is documented.
- Do not treat public web availability as redistribution permission.

## Acceptance Criteria

- Every row source ID resolves to a registry record.
- Every public release has reviewed source status.
- Risky sources are excluded or released link-only/derived-only.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial source registry specification. | SUBMITTED_TO_REVIEW |
| 2026-09-08 | Aligned documented field names with executable source configurations. | SUBMITTED_TO_REVIEW |
