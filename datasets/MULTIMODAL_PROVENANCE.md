# Multimodal Provenance Contract

## Status

Current status: `EXPERT_VALIDATED` at policy level under `KB-DATA-005`.

Current evidence gap: `NATIVE_HAITIAN_CREOLE_VISION_LANGUAGE_DATA`.

## Contract

For every multimodal item, record independently:

- media source, item identifier, immutable revision, content hash, creator/owner evidence, rights evidence, and transformations;
- caption source, immutable revision, authoring origin, original language, translation route, translator or system evidence, rights evidence, and transformations;
- media-caption linkage identifier, order, and relationship;
- parent datasets, split identity, contamination references, and downstream derivations.

Media rights and caption rights never inherit from one another.

## Authoring Origins

Use `NATIVE_HUMAN_AUTHORED`, `HUMAN_TRANSLATED`, `MACHINE_TRANSLATED`, `LLM_GENERATED`, `MIXED`, or `UNKNOWN` for caption authoring. Dataset-level content origin uses the canonical values in `ContentOrigin`, including `HUMAN_ORIGINAL`, `HUMAN_TRANSLATED`, `MACHINE_TRANSLATED`, `OCR_DERIVED`, and `UNKNOWN`.

Ordered derivation steps must preserve operations such as OCR, ASR, human transcription, translation, normalization, filtering, and adjudication. A later normalization step must not erase a prior machine-translation origin.

## Coverage Rule

XM3600 and the translated VICR lead are methodology references unless authoritative metadata establishes Haitian coverage and provenance. Translated captions cannot be reported as native Haitian Creole vision-language data. Neither resource currently contributes Haitian multimodal corpus coverage.

## Validation Gate

A frozen multimodal release requires immutable media and caption versions, hashes, source-specific rights evidence, ethics review where applicable, verified linkage, origin evidence, split identity, and contamination assessment.

