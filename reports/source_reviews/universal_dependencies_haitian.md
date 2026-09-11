# Source Review: Universal Dependencies Haitian Creole

## Review Record

- Source ID: `universal_dependencies_haitian`
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
| The official treebank page identifies UD Haitian Creole Adolphe, its release participation, CC BY-SA 4.0 label, annotation origin, and source description. | https://universaldependencies.org/treebanks/ht_adolphe/index.html | Universal Dependencies contributors | 2026-09-10 | DIRECT_FACT | HIGH |

## Findings

This is strong metadata for a specific treebank but the current registry record is still a family. The page indicates a narrow grammar-example/Bible-related source and programmatic annotation, which limits representativeness.

## Risks

The source is narrow and likely duplicated in Bible corpora or model pretraining. Programmatic annotations require quality review; share-alike and upstream-text compatibility need confirmation.

## Candidate Task Fit

NER and normalization have only indirect methodological relevance. The treebank should not be repurposed as direct evidence for those tasks without validation.

## Required Child Records

Register a version-specific UD Haitian Creole Adolphe child record with upstream-text provenance and release hashes.

## Unresolved Claims

Upstream text rights; exact release version; manual validation level; contamination; validity outside grammar examples.

## Expansion Clarification

The preceding findings describe Adolphe only, not all Haitian UD resources. Separate metadata-only records now identify `ud_haitian_adolphe` and `ud_haitian_autogramm`. The [Autogramm page](https://universaldependencies.org/treebanks/ht_autogramm/index.html) identifies different upstream texts and conversion history. No treebank count or annotation-quality claim should be generalized across them; exact releases and rights remain unapproved.

## Next Review Action

Verify license compatibility and source provenance, then assess the treebank only for clearly defined linguistic uses.

## No-Authorization Statement

This metadata review authorizes no collection, download, annotation, transformation, derived use, redistribution, scientific inclusion, release membership, or publication claim.
