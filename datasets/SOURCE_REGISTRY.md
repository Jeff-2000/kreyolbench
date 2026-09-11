# Source Registry

## Purpose

Define the open-world source inventory and the independent gates that control
how a discovered resource may be handled.

## Status

Current status: SUBMITTED_TO_REVIEW

Owner: Data Governance working group

Requires expert validation: Yes

Governing decisions: `KB-DATA-001`, `KB-DATA-003`, `KB-ENG-003`, `KB-ENG-007`

## Core Principle

The registry is not a fixed whitelist, corpus manifest, partnership list, or
statement of authorization. New resources may be registered continuously.
Registration permits metadata discovery only. Collection, annotation,
transformation, redistribution, commercial use, and scientific inclusion each
require their own documented review.

Dataset examples and retrieval documents must also satisfy
`datasets/EXAMPLE_PROVENANCE.md`. A registry record governs a source, but it
does not by itself provide sufficiently granular example provenance.

## Record Hierarchy

| Record type | Purpose | May back dataset rows? |
| --- | --- | --- |
| `SOURCE_FAMILY` | Discovery container for a provider, platform, or heterogeneous resource family | No |
| `SOURCE_COLLECTION` | Identifiable collection with coherent provenance | Yes, after applicable gates |
| `SOURCE_SUBSET` | Versioned or bounded subset of a parent family/collection | Yes, after applicable gates |

A subset requires `parent_source_id`. Families do not have parents. A family
must never receive blanket collection, redistribution, or scientific approval;
a concrete child record is required.

## Required Metadata

Every schema-v2 source record contains:

- stable ID, record type, and optional parent ID;
- name, URL, provider, and publisher/owner claim;
- data type and proposed access method;
- license label, evidence URL, evidence note, and citation instructions;
- language claim, registers, domain, temporal coverage, and geographic relevance;
- expected benchmark tasks;
- access and collection dates plus hashes when artifacts exist;
- quality, privacy, duplication, and machine-generated-content risks;
- project review status, decision references, and release-candidate flag;
- the complete `source_governance` block.

Unknown values remain `TO_VERIFY`, `UNKNOWN`, or `null`. Do not infer rights,
language coverage, ownership, partnerships, or scientific quality.

## Independent Governance Axes

| Axis | Allowed states |
| --- | --- |
| Discovery | `DISCOVERED`, `ENDPOINT_VERIFIED`, `INACCESSIBLE`, `RETIRED` |
| Access | `UNKNOWN`, `ACCESSIBLE_FOR_REVIEW`, `RESTRICTED`, `UNAVAILABLE` |
| Legal review | `NOT_STARTED`, `PENDING`, `APPROVED`, `CONDITIONAL`, `REJECTED`, `NOT_APPLICABLE` |
| Collection | `NOT_REQUESTED`, `PERMISSION_UNKNOWN`, `APPROVED`, `PROHIBITED`, `NOT_APPLICABLE` |
| Derived use | `UNKNOWN`, `APPROVED`, `CONDITIONAL`, `PROHIBITED`, `NOT_APPLICABLE` |
| Redistribution | `UNKNOWN`, `APPROVED`, `LINK_ONLY`, `DERIVED_ONLY`, `CONDITIONAL`, `PROHIBITED` |
| Commercial use | `UNKNOWN`, `APPROVED`, `CONDITIONAL`, `PROHIBITED`, `NOT_APPLICABLE` |
| Ethics | `NOT_STARTED`, `PENDING`, `APPROVED`, `RESTRICTED`, `REJECTED`, `NOT_APPLICABLE` |
| Scientific inclusion | `PENDING_EXPERT_REVIEW`, `PILOT_ONLY`, `APPROVED`, `EXCLUDED`, `NOT_APPLICABLE` |

No axis inherits approval from another. In particular, accessibility does not
authorize collection; collection does not authorize derived use or
redistribution; legal permission does not establish representativeness; and
scientific approval cannot override legal or ethical restrictions.

## Release Gate

Public source-data release requires all of the following:

- a collection or subset record, never a family;
- project status `EXPERT_VALIDATED`;
- legal review `APPROVED` or `NOT_APPLICABLE`;
- redistribution `APPROVED` with recorded evidence;
- ethics `APPROVED` or `NOT_APPLICABLE`;
- scientific inclusion `APPROVED`;
- release-candidate dependencies resolved;
- source-specific attribution, conditions, hashes, and versions recorded.

`LINK_ONLY`, `DERIVED_ONLY`, and `CONDITIONAL` are not blanket public-data
release approvals. The synthetic sample fixture is an explicit software-testing
exception: it may be committed and redistributed, but its scientific status is
`EXCLUDED` and it cannot support benchmark claims.

## Candidate Review Workflow

1. Register metadata and uncertainties.
2. Verify endpoint and provider identity.
3. Create child records for heterogeneous families.
4. Review license, ownership, platform terms, and collection permission.
5. Complete ethics and community-harm screening.
6. Assess language, quality, representativeness, duplication, and contamination.
7. Submit scientific inclusion for expert review.
8. Record collection date, version, hash, and provenance before acquisition.
9. Re-audit before annotation, derived release, or public redistribution.

## Metadata-Only Feasibility Ledger

`configs/governance/source_feasibility.yaml` records one public metadata review
for every non-synthetic candidate and a separate synthetic control. It assesses
endpoint identity, metadata accessibility, rights evidence, language/register,
provenance/versionability, ethics/privacy, provisional task fit, and
duplication/contamination.

Evidence states are `EVIDENCE_AVAILABLE`, `PARTIAL`, `MISSING`, and `BLOCKED`.
Permitted conclusions are `CONDITIONAL` and `BLOCKED`; metadata review cannot
declare a source `PILOT_FEASIBLE`. Every record must set
`authorization_effect: NONE`. Reports live under `reports/source_reviews/`, and
the consolidated packet is `reports/SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md`.

Feasibility is not an authorization axis. It prioritizes later human review and
cannot elevate legal, ethical, collection, derived-use, redistribution,
scientific, or release status.

## Discovery Intake and Evidence Version 2

See `SOURCE_DISCOVERY.md` for the open-world intake and the expanded review packet. Current feasibility schema v2 requires claim-level URLs, publisher attribution, dates and direct evidence for each EVIDENCE_AVAILABLE dimension. Historical assessments are retained, not silently overwritten. Registered sources, unresolved leads and reference-only resources are separate. Relationships never transfer rights, and reported sizes are not aggregated into unique corpus totals.

## Acceptance Criteria

- Every committed record validates against schema version 2.
- Every dataset-row source ID resolves to a collection or subset.
- Every example retains a specific provenance unit, content origin, and derivation history.
- Parent references resolve and contain no cycles.
- Approved redistribution has evidence and compatible legal and ethical states.
- Discovery-only records cannot become release candidates.
- Markdown and machine-readable decisions remain synchronized.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial source registry specification. | SUBMITTED_TO_REVIEW |
| 2026-09-08 | Aligned documented fields with executable source configurations. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Adopted open-world discovery and multi-axis schema v2; expanded candidate families without authorizing collection. | SUBMITTED_TO_REVIEW |
| 2026-09-09 | Linked source governance to the example-level provenance contract. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Added complete metadata-only feasibility coverage and machine-enforced no-authorization rules. | SUBMITTED_TO_REVIEW |
