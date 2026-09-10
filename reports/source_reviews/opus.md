# Source Review: OPUS Parallel Corpora

## Review Record

- Source ID: `opus`
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
