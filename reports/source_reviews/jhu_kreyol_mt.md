# Source Review: JHU Kreyol-MT

## Review Record

- Source ID: `jhu_kreyol_mt`
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
| The official dataset card identifies a multilingual Creole MT collection, 74 listed subsets, and an aggregate license value of `other`. | https://huggingface.co/datasets/jhu-clsp/kreyol-mt | JHU CLSP | 2026-09-10 | DIRECT_FACT | HIGH |
| The primary NAACL paper documents the research resource. | https://aclanthology.org/2024.naacl-long.170/ | ACL Anthology / paper authors | 2026-09-10 | DIRECT_FACT | HIGH |

## Findings

The collection is versioned and accessible at metadata level, but the card states that upstream license/release information varies and that sentence-source metadata is incomplete or planned. Aggregate visibility does not establish Haitian-subset reuse rights.

## Risks

Parallel text may include machine translation, religious material, duplicates, and sources already present in pretraining. Mixing Creole varieties would invalidate Haitian Creole claims.

## Candidate Task Fit

No direct fit to the five current pilot tasks is asserted because translation is deferred. The resource remains relevant to future MT and contamination analysis.

## Required Child Records

Register each Haitian Creole language pair and each upstream corpus separately before any use.

## Unresolved Claims

Haitian Creole subset inventory; upstream terms; sentence provenance; versions; machine-generated origin; overlap with OPUS/eBible/NLLB.

## Next Review Action

Review the official source documentation and select only provenance-complete Haitian child subsets for later human review.

## No-Authorization Statement

This metadata review authorizes no collection, download, annotation, transformation, derived use, redistribution, scientific inclusion, release membership, or publication claim.
