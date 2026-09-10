# Data Governance

Every source must have a schema-v2 YAML registry entry with provenance, access
method, license evidence, language/register claims, domain, dates, hashes, and
risk metadata. The normative schema and release gate are defined in
`datasets/SOURCE_REGISTRY.md`.

## Rules

- Discovery and registration do not authorize content collection.
- Do not commit raw external text unless redistribution is explicitly approved.
- Keep raw, clean, and normalized text separate.
- Store source URL and retrieval date on every row.
- Run PII detection before public release.
- Keep annotator audit logs private if they contain personal information.
- Preserve source-specific attribution requirements and conditions.
- Register concrete OPUS, CreoleVal, government, media, and institutional subsets separately.

## Review Dimensions

Do not use the deprecated single `review_status`. Source discovery, access,
legal review, collection, derived use, redistribution, commercial use, ethics,
and scientific inclusion are independent dimensions. Approval on one dimension
never implies approval on another.
