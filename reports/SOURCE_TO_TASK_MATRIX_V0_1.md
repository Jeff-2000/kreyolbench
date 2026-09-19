# Metadata-Only Source-to-Task Matrix v0.1

## Status

Current status: SUBMITTED_TO_REVIEW

Authorization effect: NONE

This matrix records plausible research relevance, not source approval or task readiness. `CANDIDATE` means the metadata suggests possible fit; `INDIRECT` means the source may support comparison, terminology, or robustness work; `NO_CURRENT_FIT` means no fit to the five provisional v0.1 tasks was asserted.

| Source | Classification | NER | Retrieval | Normalization | Code-switching | Limiting evidence |
| --- | --- | --- | --- | --- | --- | --- |
| AKA official/publications | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | CANDIDATE | NO_CURRENT_FIT | Document rights and normative authority per version. |
| Haitian government portal/family | CANDIDATE | CANDIDATE | CANDIDATE | NO_CURRENT_FIT | NO_CURRENT_FIT | Portal is accessible; asset-level CC0 applicability, third-party rights, Kreyol coverage, and family boundaries remain unresolved. |
| MSPP | CANDIDATE | CANDIDATE | CANDIDATE | NO_CURRENT_FIT | NO_CURRENT_FIT | Document rights, provenance, and health-risk review. |
| MENFP | CANDIDATE | CANDIDATE | CANDIDATE | NO_CURRENT_FIT | NO_CURRENT_FIT | Endpoint, rights, language mix, and minors-related review. |
| Civil Protection | NO_CURRENT_FIT | NO_CURRENT_FIT | CANDIDATE | NO_CURRENT_FIT | NO_CURRENT_FIT | Endpoint and item inventory unresolved. |
| UN Haiti | CANDIDATE | CANDIDATE | CANDIDATE | NO_CURRENT_FIT | NO_CURRENT_FIT | Mixed-language assets and asset-specific terms. |
| Wikimedia HT | CANDIDATE | CANDIDATE | CANDIDATE | NO_CURRENT_FIT | NO_CURRENT_FIT | Attribution, imported-content exceptions, contamination. |
| Radio Haiti archive/corpus | NO_CURRENT_FIT | INDIRECT | NO_CURRENT_FIT | INDIRECT | CANDIDATE | Item rights, ethics, transcripts, and corpus license. |
| VoxLingua107 Haitian | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | INDIRECT | Speech-language-ID resource only; transcripts, consent, rights, and regional representation unresolved. |
| Northern Haitian Creole corpus | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | INDIRECT | CANDIDATE | Regional relevance is high, but access, custodian, consent, transcript status, and exact sampling remain blocked. |
| Mission 4636 open/non-sensitive child | CANDIDATE | INDIRECT | CANDIDATE | CANDIDATE | CANDIDATE | Exact artifact, privacy-selection evidence, residual sensitivity, translation history, and custodian terms unresolved. |
| Mission 4636 restricted/sensitive child | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | Prohibited from ordinary pipelines pending custodian and formal ethics authorization. |
| MIT-Ayiti | CANDIDATE | NO_CURRENT_FIT | CANDIDATE | INDIRECT | NO_CURRENT_FIT | Asset-specific rights and provenance. |
| CreoleVal | INDIRECT | INDIRECT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | Upstream-subset licensing and benchmark overlap. |
| CMU | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | Current endpoint and subset inventory unavailable. |
| Kreyol-MT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | MT is deferred; subset licenses and provenance unresolved. |
| OPUS | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | Family requires corpus-level children; MT is deferred. |
| UD Haitian | NO_CURRENT_FIT | INDIRECT | NO_CURRENT_FIT | INDIRECT | NO_CURRENT_FIT | Narrow grammar/Bible origin and contamination. |
| eBible | NO_CURRENT_FIT | INDIRECT | NO_CURRENT_FIT | INDIRECT | NO_CURRENT_FIT | Narrow domain and likely benchmark/pretraining overlap. |
| Haitian media | CANDIDATE | CANDIDATE | NO_CURRENT_FIT | CANDIDATE | CANDIDATE | No publisher-specific record exists. |
| Diaspora publications | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | CANDIDATE | CANDIDATE | No publisher-specific record exists. |
| Social media | NO_CURRENT_FIT | NO_CURRENT_FIT | NO_CURRENT_FIT | CANDIDATE | CANDIDATE | Ethics and platform terms are not scoped. |

## Interpretation Rules

- This matrix cannot promote a source or task status.
- A source family must be replaced by a collection or subset record before example-level provenance can reference it.
- Task relevance must be re-evaluated after source content, rights, register, and representativeness are known through authorized review.
- No data acquisition or annotation follows from a `CANDIDATE` cell.

## Required Evidence for Every Future Source-to-Task Proposal

| Dimension | Required record before pilot authorization |
| --- | --- |
| Construct relevance | Explain why the source elicits the task construct rather than merely sharing a topic or format. |
| Language authenticity | Document Haitian Creole origin, translation route, register, and uncertainty; language labels alone are insufficient. |
| Sampling appropriateness | Define bounded sampling frame, dates, publisher or community coverage, and exclusions. |
| Annotation feasibility | Identify the annotation unit, native-speaker or domain-expert requirements, ambiguity, privacy, and adjudication burden. |
| Domain effects | State how institutional, religious, educational, journalistic, historical, or translated registers limit interpretation. |
| Leakage and contamination | Link source, version, split, hashes, known relationships, and the contamination registry. |
| Representativeness | State which Haitian Creole varieties, periods, geographies, and registers are absent; do not generalize from family metadata. |

Speech, syntax, translation, multimodal, educational, historical, and diaspora resources remain valid open-world research pathways even when they have no direct v0.1 task fit. `NO_CURRENT_FIT` is not a scientific exclusion.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-10 | Initial metadata-only source-to-task matrix. | SUBMITTED_TO_REVIEW |
| 2026-09-18 | Added construct-level evidence requirements and corrected government-portal feasibility. | SUBMITTED_TO_REVIEW |
| 2026-09-19 | Added Project-Lead-reviewed speech and Mission 4636 source distinctions without authorizing use. | SUBMITTED_TO_REVIEW |
