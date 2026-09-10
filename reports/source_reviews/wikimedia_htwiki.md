# Source Review: Haitian Creole Wikipedia Dumps

## Review Record

- Source ID: `wikimedia_htwiki`
- Registry type: `SOURCE_COLLECTION`
- Review status: `SUBMITTED_TO_REVIEW`
- Overall conclusion: `CONDITIONAL`
- Reviewed on: 2026-09-10
- Prepared by: Codex
- AI assistance disclosed: true
- Authorization effect: `NONE`

## Authoritative Evidence

| Claim | URL | Publisher | Access date | Basis | Confidence |
| --- | --- | --- | --- | --- | --- |
| Wikimedia terms describe attribution and share-alike licensing for user-contributed text, with exceptions for imported and non-text content. | https://foundation.wikimedia.org/wiki/Policy:Terms_of_Use | Wikimedia Foundation | 2026-09-10 | DIRECT_FACT | HIGH |
| Wikimedia publishes a Haitian Creole Wikipedia dump endpoint. | https://dumps.wikimedia.org/htwiki/latest/ | Wikimedia Foundation | 2026-09-10 | DIRECT_FACT | HIGH |

## Findings

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
