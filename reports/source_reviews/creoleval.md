# Source Review: CreoleVal

## Review Record

- Source ID: `creoleval`
- Registry type: `SOURCE_FAMILY`
- Review status: `SUBMITTED_TO_REVIEW`
- Overall conclusion: `CONDITIONAL`
- Reviewed on: 2026-09-10
- Prepared by: Codex
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
