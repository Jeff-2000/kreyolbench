# Data Governance

Every source must have a YAML registry entry with URL, access method, license, redistribution status, citation, language claim, domain, collection date, hash, PII risk, and review status.

## Rules

- Do not commit raw external text unless redistribution is allowed.
- Keep raw, clean, and normalized text separate.
- Store source URL and retrieval date on every row.
- Run PII detection before public release.
- Keep annotator audit logs private if they contain personal information.
- Preserve attribution requirements for Wikimedia, OPUS subsets, and other upstream data.

## Review Status Values

- `reviewed_public_domain_notice`
- `reviewed_standard_wikimedia_terms`
- `pending_legal_review`
- `pending_subset_review`
- `not_approved_for_redistribution`

