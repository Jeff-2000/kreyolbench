# Source Review: Haitian Creole Wikipedia Dumps

## Review Record

- Source ID: `wikimedia_htwiki`
- Registry type: `SOURCE_COLLECTION`
- Review status: `SUBMITTED_TO_REVIEW`
- Scientific feasibility summary: `CONDITIONAL` (non-authoritative; independent governance axes control use)
- Current review updated on: 2026-09-18
- Implemented by: Codex, with Project-Lead decision attributed separately
- AI assistance disclosed: true
- Authorization effect: `NONE`

## Authoritative Evidence

| Claim | URL | Publisher | Access date | Basis | Confidence |
| --- | --- | --- | --- | --- | --- |
| Wikimedia terms describe attribution and share-alike licensing for user-contributed text, with exceptions for imported and non-text content. | https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use | Wikimedia Foundation | 2026-09-10 | DIRECT_FACT | HIGH |
| Wikimedia publishes a Haitian Creole Wikipedia dump endpoint. | https://dumps.wikimedia.org/htwiki/latest/ | Wikimedia Foundation | 2026-09-10 | DIRECT_FACT | HIGH |

## Findings

The existing `wikimedia_htwiki_20231101` child supplies snapshot identity. Any future provenance must also retain extraction code and version, page and revision IDs, title, namespace, redirect status, content hash, attribution mechanism, imported-content notices, and deletion or revision handling.

The collection has strong provider, language-route, licensing-framework, and snapshotability evidence. Page-level attribution, imported-content exceptions, revisions, and non-text licenses still require explicit handling.

## Risks

Wikipedia is heavily represented in multilingual pretraining and benchmarks, creating contamination risk. Article quality and register are uneven; personal biographies can contain sensitive or contested claims.

## Candidate Task Fit

Classification, NER, and retrieval are plausible. Any test set requires contamination analysis, snapshot IDs, page revisions, and attribution-preserving release design.

## Required Child Records

Register one immutable dump snapshot and extraction policy, excluding content whose licensing or provenance cannot be represented.

## Unresolved Claims

Exact snapshot; attribution mechanics; imported text and media exceptions; deleted/revised pages; model pretraining overlap.

## Next Review Action

Design a snapshot-specific child subset and obtain legal and scientific review before extraction.

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

Use only an immutable snapshot child with page and revision provenance, attribution, imported-content exceptions, and contamination analysis.

## Review History

- 2026-09-10: `ORIGINAL_CODEX_METADATA_ASSESSMENT`; AI-assisted metadata triage; no human scientific decision.
- 2026-09-18: `PROJECT_LEAD_REVIEW_DECISION`; Jeff Pierre; `RETAIN_CONDITIONAL`.
- 2026-09-18: `IMPLEMENTATION_EVIDENCE_CHECK`; Codex; public authoritative metadata checked without making a human or independent approval.
