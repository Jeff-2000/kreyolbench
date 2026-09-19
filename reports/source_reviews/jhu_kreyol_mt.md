# Source Review: JHU Kreyol-MT

## Review Record

- Source ID: `jhu_kreyol_mt`
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
| The official dataset card identifies a multilingual Creole MT collection, 74 listed subsets, and an aggregate license value of `other`. | https://huggingface.co/datasets/jhu-clsp/kreyol-mt | JHU CLSP | 2026-09-10 | DIRECT_FACT | HIGH |
| The primary NAACL paper documents the research resource. | https://aclanthology.org/2024.naacl-long.170/ | ACL Anthology / paper authors | 2026-09-10 | DIRECT_FACT | HIGH |
| The repository tree includes `hat-ara`, `hat-aze`, `hat-deu`, `hat-eng`, `hat-fra`, `hat-nep`, and `hat-zho` directories. | https://huggingface.co/datasets/jhu-clsp/kreyol-mt/tree/main | JHU CLSP | 2026-09-18 | IMPLEMENTATION_EVIDENCE_CHECK | HIGH |

## Findings

The collection is versioned and accessible at metadata level, but the card states that upstream license/release information varies and that sentence-source metadata is incomplete or planned. Aggregate visibility does not establish Haitian-subset reuse rights.

## Risks

Parallel text may include machine translation, religious material, duplicates, and sources already present in pretraining. Mixing Creole varieties would invalidate Haitian Creole claims.

## Candidate Task Fit

No direct fit to the five current pilot tasks is asserted because translation is deferred. The resource remains relevant to future MT and contamination analysis.

## Required Child Records

Register each Haitian Creole language pair and each upstream corpus separately before any use.

## Unresolved Claims

Exact revision and selected Haitian language-pair children; upstream terms; sentence provenance; versions; human or machine-translated origin; overlap with OPUS/eBible/NLLB.

## Next Review Action

Review the official source documentation and select only provenance-complete Haitian child subsets for later human review.

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

Register each selected Haitian language pair and upstream component; audit origin, license, duplicate, split, and contamination status.

## Review History

- 2026-09-10: `ORIGINAL_CODEX_METADATA_ASSESSMENT`; AI-assisted metadata triage; no human scientific decision.
- 2026-09-18: `PROJECT_LEAD_REVIEW_DECISION`; Jeff Pierre; `RETAIN_CONDITIONAL`.
- 2026-09-18: `IMPLEMENTATION_EVIDENCE_CHECK`; Codex; public authoritative metadata checked without making a human or independent approval.
