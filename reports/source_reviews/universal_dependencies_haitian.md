# Source Review: Universal Dependencies Haitian Creole

## Review Record

- Source ID: `universal_dependencies_haitian`
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
| The official treebank page identifies UD Haitian Creole Adolphe, its release participation, CC BY-SA 4.0 label, annotation origin, and source description. | https://universaldependencies.org/treebanks/ht_adolphe/index.html | Universal Dependencies contributors | 2026-09-10 | DIRECT_FACT | HIGH |
| The official page identifies Autogramm as a distinct Haitian Creole treebank available since UD v2.13 under CC BY-SA 4.0, with Bible, literary, and newspaper sources. | https://universaldependencies.org/treebanks/ht_autogramm/index.html | Universal Dependencies contributors | 2026-09-18 | IMPLEMENTATION_EVIDENCE_CHECK | HIGH |
| The official page identifies Adolphe as a distinct Haitian Creole treebank available since UD v2.16 under CC BY-SA 4.0, derived from a Bible-related source. | https://universaldependencies.org/treebanks/ht_adolphe/index.html | Universal Dependencies contributors | 2026-09-18 | IMPLEMENTATION_EVIDENCE_CHECK | HIGH |

## Findings

The family has two registered child records, `ud_haitian_autogramm` and `ud_haitian_adolphe`. Their official metadata establish distinct release histories, source mixtures, and annotation/conversion histories. Treebank-level CC BY-SA 4.0 notices do not eliminate upstream-text review.

## Risks

The source is narrow and likely duplicated in Bible corpora or model pretraining. Programmatic annotations require quality review; share-alike and upstream-text compatibility need confirmation.

## Candidate Task Fit

NER and normalization have only indirect methodological relevance. The treebank should not be repurposed as direct evidence for those tasks without validation.

## Required Child Records

Pin exact UD release versions and repository commits or hashes for the existing Autogramm and Adolphe child records.

## Unresolved Claims

Upstream text rights; exact release version; manual validation level; contamination; validity outside grammar examples.

## Expansion Clarification

The preceding findings describe Adolphe only, not all Haitian UD resources. Separate metadata-only records now identify `ud_haitian_adolphe` and `ud_haitian_autogramm`. The [Autogramm page](https://universaldependencies.org/treebanks/ht_autogramm/index.html) identifies different upstream texts and conversion history. No treebank count or annotation-quality claim should be generalized across them; exact releases and rights remain unapproved.

## Next Review Action

Verify license compatibility and source provenance, then assess the treebank only for clearly defined linguistic uses.

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

Pin exact UD release and commit or hash and review Autogramm and Adolphe upstream-text rights independently.

## Review History

- 2026-09-10: `ORIGINAL_CODEX_METADATA_ASSESSMENT`; AI-assisted metadata triage; no human scientific decision.
- 2026-09-18: `PROJECT_LEAD_REVIEW_DECISION`; Jeff Pierre; `RETAIN_CONDITIONAL`.
- 2026-09-18: `IMPLEMENTATION_EVIDENCE_CHECK`; Codex; public authoritative metadata checked without making a human or independent approval.
