# Data Access Policy

KreyolBench uses controlled data access. Code can be open-source, but data access depends on license, consent, privacy risk, redistribution status, and project need.

This policy complements `docs/data_governance.md` and `docs/ethics.md`.

## Data Classes

### Public Data

Data that can be redistributed under its license and has passed PII and ethics review.

Examples:

- Tiny sample fixtures.
- Synthetic examples.
- Public-domain text with documented source metadata.
- Released benchmark splits approved for redistribution.

### Link-Only Data

Data that can be referenced but not redistributed directly.

Examples:

- Public webpages with unclear redistribution terms.
- Third-party corpora requiring download from original host.

### Derived-Only Data

Data where only derived features, metadata, labels, or evaluation outputs may be released.

Examples:

- Corpora with restricted redistribution but permitted research use.
- Sources where text cannot be republished.

### Internal Research Data

Data approved only for a named research team or internal analysis.

Examples:

- Partner-provided corpora.
- Unpublished annotations.
- Non-public public-sector documents.

### Restricted Sensitive Data

Data requiring explicit project-lead and data-steward approval.

Examples:

- Raw speech.
- Consent records.
- Annotator identity.
- Human-subject data.
- Private communications.
- PII-risk records.

## Access Requirements

Every request for non-public data must document:

- Requester name and affiliation.
- Project role.
- Data requested.
- Purpose.
- Duration of access.
- Storage location.
- Whether export, download, or redistribution is needed.
- Agreement to follow project data rules.

## Access Approval

- Public data: no approval beyond license compliance.
- Link-only or derived-only data: maintainer or data-steward review.
- Internal research data: project-lead approval.
- Restricted sensitive data: project-lead and data-steward approval.

## Storage Rules

- Do not commit restricted or raw external data to Git.
- Keep raw, interim, processed, normalized, and public-release data separate.
- Store restricted data in controlled storage with access logs.
- Separate consent/payment records from research data.
- Remove access when no longer needed.

## Release Rules

Before any dataset release:

- Source registry entries must be complete.
- License review must be complete.
- PII scan must be complete and documented.
- Deduplication report must be generated.
- Splits must be frozen and hashed.
- Dataset card must be updated.
- Known limitations must be documented.

## Prohibited Uses

KreyolBench data must not be used for surveillance, harmful profiling, automated denial of public services, or targeting based on language, dialect, geography, politics, or migration status.

