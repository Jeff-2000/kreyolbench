# Source Discovery Contract

## Purpose and Status

Current status: TO_REVIEW_LATER

Engineering decision: KB-ENG-008. Findings require human review; no source permission changes.

## Registries

- `configs/governance/source_discovery.yaml`: deduplicated intake, disposition, evidence, candidate roles, reported sizes and relationships.
- `configs/sources/`: schema-v2 source identity and independent authorization axes.
- `configs/governance/source_feasibility.yaml`: schema-v2 claim-level evidence for every current non-synthetic source plus a separate test control.
- `reports/source_reviews/history/`: historical review and authorization snapshots; not active configuration.

## Identity and Disposition

Canonical URL, configuration and revision identify one lead. Repeated user mentions map to that lead. Different snapshots and derivatives retain different records. REGISTERED_SOURCE requires an existing source ID and direct metadata evidence of Haitian coverage; it does not validate language quality. UNVERIFIED_LEAD is retained when identity, coverage or release metadata is insufficient. REFERENCE_ONLY records scholarly or methodology relevance without claiming a Haitian corpus. APiCS survey and structured contribution remain separate references.

Intake records preserve supplied lead IDs independently of later disposition changes. Future intake expansion is open-world, not a fixed whitelist or count. Do not remove an intake to make a coverage test pass.

## Evidence Contract

Each EVIDENCE_AVAILABLE feasibility dimension requires a direct limited claim, HTTP(S) evidence URL, publisher and access date. The URL must also occur in the record's evidence list. Inference alone remains PARTIAL. Dates must be valid, not future-dated, and not later than the review. An official badge is evidence of a displayed assertion, not a legal conclusion.

A parser cannot verify truth or publisher authority. Human review must examine whether the actual page supports the claim. Preserve uncertainty and unavailable endpoints. No corpus rows, recordings, dumps or model artifacts may be fetched by the audit.

## Roles and Provenance

Roles describe possible training, evaluation, linguistic, speech and multimodal uses without authorizing them. Family and domain IDs resolve through open-world registries; candidate task-instance IDs are optional. Mapping to a roadmap family creates no runtime implementation or release membership.

Content origin reuses the example-provenance enum. Non-UNKNOWN origins require evidence; language tags, provider reputation and corpus size are not sufficient. Collection-level origin never overrides later example-level provenance.

SNAPSHOT_OF, CLAIMED_DERIVATIVE_OF, HOSTED_WITHIN, ORIGINATES_FROM and POSSIBLE_SHARED_UPSTREAM relationships require source references and evidence. Hosting is not ownership. Mirrors never inherit rights or approval. Possible overlap is an investigation question, not a measured overlap rate.

## Size and Contamination

Reported size requires value, unit, configuration, split, revision, attribution and verification state. UNKNOWN details use TO_VERIFY rather than guessed values. No aggregate unique-corpus total is computed. Keep upstream evaluation partitions identifiable and require contamination review before any proposal to reuse evaluation content for training.

## Acceptance Criteria

- All intake leads have exactly one disposition; all registered candidates have feasibility coverage.
- Evidence paths stay inside the repository and exist.
- Source, family, domain and task references resolve.
- Existing source authorization states and release membership remain unchanged by this expansion.
- Synthetic controls remain separate and scientifically excluded.
- Findings remain SUBMITTED_TO_REVIEW or BLOCKED; structural PASS is not scientific approval.

## Next Recommended Action

Human review of the expansion packet, followed by metadata clarification and source-specific legal/ethics review. No acquisition or pilot is authorized.

## Revision History

- 2026-09-10: Established discovery intake and feasibility-v2 evidence requirements.
