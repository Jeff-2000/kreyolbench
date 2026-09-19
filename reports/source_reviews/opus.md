# Source Review: OPUS Parallel Corpora

## Review Record

- Source ID: `opus`
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
| OPUS exposes a public catalog of many multilingual parallel corpora. | https://opus.nlpl.eu/corpora | OPUS | 2026-09-10 | DIRECT_FACT | HIGH |

## Findings

OPUS is an aggregation family, not a single licensed source. Haitian Creole availability, versions, upstream ownership, domains, alignment methods, and terms must be evaluated per named corpus.

## Risks

Subcorpora may duplicate eBible, UN, subtitles, localization, or MT resources and may contain noisy or machine-generated alignments. Benchmark leakage risk is high.

## Candidate Task Fit

No direct fit to the five current pilot tasks is asserted. Future MT or robustness use requires a named Haitian Creole child corpus.

## Required Child Records

Create a child record for each selected corpus, version, language pair, and upstream source.

## Unresolved Claims

Haitian Creole catalog entries; per-corpus license; release version; alignment origin; duplicates; machine generation.

## Next Review Action

Perform catalog-only discovery, then register selected child corpora for separate human review.

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

Register corpus, version, language pair, and upstream source children before any provenance or use decision.

## Review History

- 2026-09-10: `ORIGINAL_CODEX_METADATA_ASSESSMENT`; AI-assisted metadata triage; no human scientific decision.
- 2026-09-18: `PROJECT_LEAD_REVIEW_DECISION`; Jeff Pierre; `RETAIN_CONDITIONAL`.
