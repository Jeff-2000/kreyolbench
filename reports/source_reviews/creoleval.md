# Source Review: CreoleVal

## Review Record

- Source ID: `creoleval`
- Registry type: `SOURCE_FAMILY`
- Review status: `SUBMITTED_TO_REVIEW`
- Scientific feasibility summary: `CONDITIONAL` (non-authoritative; independent governance axes control use)
- Current review updated on: 2026-09-18
- Implemented by: Codex, with Project-Lead decision attributed separately
- AI assistance disclosed: true
- Authorization effect: `NONE`

## Authoritative Evidence

| Claim | URL | Publisher | Access date | Basis | Confidence |
| --- | --- | --- | --- | --- | --- |
| The official repository presents CreoleVal as a multi-task Creole evaluation resource and identifies heterogeneous component datasets. | https://github.com/hclent/CreoleVal | CreoleVal authors | 2026-09-10 | DIRECT_FACT | HIGH |
| The primary TACL paper documents the benchmark research contribution. | https://aclanthology.org/2024.tacl-1.53/ | ACL Anthology / paper authors | 2026-09-10 | DIRECT_FACT | HIGH |

## Findings

CreoleVal is scientifically relevant for comparison and prior-art analysis, but it is a family of upstream resources with different provenance and rights. A repository-level license cannot be assumed to govern every component.

## Risks

Reuse can introduce direct test overlap, translated-data artifacts, and benchmark contamination. Haitian Creole subsets may not match KreyolBench constructs or domains.

## Candidate Task Fit

Classification and NER are indirect comparison candidates. Task and label compatibility must be demonstrated rather than inferred from similar task names.

## Required Child Records

Register every considered Haitian Creole component as its own subset with upstream source, version, license, and split hashes.

## Unresolved Claims

Upstream licenses; Haitian Creole subset provenance; label compatibility; translation origin; train/test overlap.

## Next Review Action

Select candidate components only as metadata and conduct subset-level legal and contamination review.

## No-Authorization Statement

This metadata review authorizes no collection, download, annotation, transformation, derived use, redistribution, scientific inclusion, release membership, or publication claim.

## Project-Lead Review Event

- Event type: `PROJECT_LEAD_REVIEW_DECISION`
- Reviewer: Jeff Pierre
- Role: Project Lead and Scientific Reviewer
- Review date: 2026-09-18
- Independence: `INTERNAL_PROJECT_LEAD`
- Decision: `RETAIN_CONDITIONAL`
- Scientific feasibility after review: `CONDITIONAL`
- Authorization effect: `NONE`

This is a human Project-Lead feasibility and prioritization decision. It does not approve collection, transformation, annotation, derived use, redistribution, scientific inclusion, release membership, or publication claims.

## External Evidence Required

Source-specific rights, provenance, version, legal, ethical, linguistic, contamination, and representativeness questions remain open where applicable. Repository inspection cannot substitute for rights-holder clarification, legal counsel, ethics review, archive or source-owner confirmation, or qualified Haitian Creole review.

Consequence if unresolved: no collection, annotation, derived use, redistribution, scientific inclusion, or release.

## Exact Next Action

Audit every Haitian component for upstream identity, version, origin, license, split, hashes, construct compatibility, and overlap.

## Review History

- 2026-09-10: `ORIGINAL_CODEX_METADATA_ASSESSMENT`; AI-assisted metadata triage; no human scientific decision.
- 2026-09-18: `PROJECT_LEAD_REVIEW_DECISION`; Jeff Pierre; `RETAIN_CONDITIONAL`.
