# Example-Level Provenance Contract

Canonical `origin_type` values are `HUMAN_ORIGINAL`, `HUMAN_TRANSLATED`, `MACHINE_TRANSLATED`, `LLM_GENERATED`, `SYNTHETIC_OTHER`, `ASR_DERIVED`, `OCR_DERIVED`, `HUMAN_TRANSCRIBED`, `MIXED`, and `UNKNOWN`.

Origin is not the same as derivation. Preserve ordered `derivation_steps` for OCR, ASR, human transcription, normalization, translation, filtering, and other transformations. A downstream transformation must not overwrite deeper content origin.

For image-text or other multimodal artifacts, apply `MULTIMODAL_PROVENANCE.md`; media rights and caption rights are independent.

## Purpose

Define persistent provenance for every benchmark example and retrieval document. This contract implements conditions 7 and 8 of validated decision `KB-DATA-001`; it does not grant permission to use any source.

## Status

Current status: TO_REVIEW_LATER

Owner: Data Governance working group

Requires expert validation: No for the engineering contract; source-specific facts require review

## Scope

Source-registry records describe candidate families, collections, and subsets. Example provenance identifies the specific permitted unit from which benchmark content was derived. The private research record may be more detailed than a public release view when disclosure would create privacy, security, or contractual risk.

## Required Fields

| Field | Requirement |
| --- | --- |
| `source_id` | Must resolve to a `SOURCE_COLLECTION` or `SOURCE_SUBSET`; a family is invalid. |
| `provenance_unit_id` | Stable project identifier for the most specific permitted source unit. |
| `source_item_locator` | Reproducible item locator or controlled internal locator; never invent a public URL. |
| `source_version` | Source release, snapshot, retrieval batch, or documented `UNKNOWN`. |
| `retrieved_at` | ISO date for acquisition or fixture creation. |
| `content_hash` | SHA-256 digest of the governed source representation. |
| `origin_type` | Primary origin category defined below. |
| `derivation_steps` | Ordered transformations between source and benchmark representation. |

## Origin Types

- `HUMAN_ORIGINAL`: originally produced by a person in the recorded language and modality.
- `HUMAN_TRANSLATION`: translated by a person from another language.
- `MACHINE_TRANSLATION`: produced principally through machine translation.
- `LLM_GENERATED`: generated principally by a language model.
- `SYNTHETIC`: deliberately constructed fixture or controlled synthetic example.
- `MIXED`: multiple origin routes cannot be separated at the example level.
- `UNKNOWN`: evidence is insufficient; this must not be silently upgraded.

Origin describes authorship history. It does not replace derivation history. For example, a human-original radio utterance transcribed by ASR remains `HUMAN_ORIGINAL` with an `ASR` derivation step.

## Derivation Steps

Allowed initial step types are `MANUAL_TRANSCRIPTION`, `ASR`, `OCR`, `NORMALIZATION`, `HUMAN_TRANSLATION`, `MACHINE_TRANSLATION`, `LLM_GENERATION`, and `OTHER`.

Each step records a stable step ID, contiguous sequence number, type, tool or responsible agent when known, version when relevant, reviewer when reviewed, and notes. A material transformation must never be hidden in generic preprocessing metadata.

## Privacy and Release Views

- Preserve the full locator in controlled records when needed for auditability.
- Publish a redacted stable locator when an item URL, speaker identifier, or document identifier is sensitive.
- Do not place consent records, annotator identities, access logs, or restricted locators in public dataset rows.
- A content hash supports integrity checks but does not establish copyright status, consent, or scientific suitability.

## Scientific Requirements

- Preserve raw/source text separately from normalized or annotated derivatives.
- Link multiple benchmark examples derived from the same source unit so split logic can group them.
- Record translation, transcription, OCR, ASR, and generation routes where determinable.
- Treat `UNKNOWN` and `MIXED` as analysis strata in contamination and robustness reviews.
- Use `CONTAMINATION_NOT_ESTABLISHED`, never `CONTAMINATION_FREE`, when overlap has not been demonstrated but absence cannot be proven.
- Do not use synthetic fixtures as benchmark evidence.

## Acceptance Criteria

- Every committed sample row validates against the typed provenance model.
- Retrieval documents use the same provenance contract.
- Family-level source IDs are rejected.
- Derivation sequences are contiguous and step IDs are unique.
- Release documentation explains any redacted locator policy.

## Known Risks

- A locator can expose sensitive identity or restricted access paths.
- Transformation records may be incomplete for inherited corpora.
- A hash can create false confidence if the governed representation is undefined.
- `UNKNOWN` origin may limit analyses of translation or machine-generation artifacts.

## Next Recommended Action

Define the private/public provenance projection before real source acquisition and validate it through one legally approved pilot subset.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Added typed example provenance and content-origin requirements. | TO_REVIEW_LATER |
| 2026-09-18 | Linked example provenance to source contamination and diversity accounting. | TO_REVIEW_LATER |
