# Named Entity Recognition Specification

## Status

Current status: SUBMITTED_TO_REVIEW

Decision: `KB-TASK-NER-001`

Task instance: `kb_ie_ner_charspan_v0_1`

Task family / type / variant: information extraction / named entity recognition / character spans with optional nesting

Scope status: PILOT_CANDIDATE for v0.1

Owner: NER working group

Required external review: Haitian Creole linguist and NER methodology expert

This specification defines one provisional v0.1 NER instance, not the complete information-extraction family. Future reviewed instances may be flat, nested, discontinuous, relation-based, event-based, or entity-linking tasks.

## Purpose and Construct

Measure exact identification and typing of named or domain-salient entities in Haitian Creole text. Canonical gold annotations use Unicode character offsets over preserved raw text so validity does not depend on a particular tokenizer.

## Research Value and Use Cases

- Extract Haitian institutions, places, events, policies, and health concepts.
- Evaluate multilingual transfer under Haitian orthographic and naming variation.
- Support search and corpus analysis while avoiding automated decisions about individuals.

## Canonical Contract

```json
{
  "input":{"text":"MSPP anonse yon kanpay nan Pòtoprens."},
  "target":{"entities":[
    {"entity_id":"e1","start_char":0,"end_char":4,"text":"MSPP","label":"ORG"},
    {"entity_id":"e2","start_char":27,"end_char":36,"text":"Pòtoprens","label":"GPE"}
  ]}
}
```

Offsets are zero-based, start-inclusive, end-exclusive Unicode code-point indices over immutable raw text. Unicode normalization or preprocessing must never silently change that coordinate space. The schema can represent nested spans, but routine nested annotation is disabled unless pilot evidence and external review activate it. Crossing spans and duplicate boundaries are prohibited. Each canonical span has one type. A tokenizer and BIO/BILOU representation may be exported only as a versioned derivative, with losses from nesting documented.

## Candidate Entity Types

Current candidates are `PER`, `ORG`, `LOC`, `GPE`, `DATE`, `TIME`, `MONEY`, `PERCENT`, `FACILITY`, `HEALTH_CONDITION`, `PRODUCT`, `LAW_POLICY`, and `EVENT`. Versioned candidate definitions are in `configs/labels/ner.yaml`. External review must resolve `LOC` versus `GPE`, organizations versus facilities, named diseases versus generic conditions, and policy titles versus descriptive phrases.

## Boundary and Nesting Rules

- Annotate the minimal complete referring expression unless a reviewed type rule requires a larger span.
- Exclude leading determiners unless they are part of the official name.
- Preserve accents, apostrophes, hyphens, abbreviations, and spelling as written.
- Permit nesting only when both spans have independently meaningful reviewed types.
- Record metonymy, demonym, acronym, and ambiguous-title cases for adjudication.
- Do not infer an entity from external knowledge when it is not expressed in the text.
- Score only contiguous spans in v0.1. Flag discontinuous mentions as `DISCONTINUOUS_UNSUPPORTED`, preserve them in the adjudication record, and exclude them from scored gold rather than forcing an invalid contiguous boundary.
- Treat the character-span representation as an internally endorsed design direction, not external scientific validation of the ontology or task.

## Inclusion and Exclusion

Include texts with interpretable context and permitted provenance. Exclude severe OCR/ASR corruption until the derivation quality is reviewed. Personal data require ethical and release review even when an entity can be annotated technically.

## Annotation and Quality Control

Use a span-capable tool preserving raw offsets. Independently annotate a pilot stratified by domain and register. Compare exact boundary/type agreement, partial overlap patterns, and per-type agreement. Preserve original annotations before adjudication. Haitian names, institutions, locations, and language-specific boundaries require Haitian expert review.

## Sources and Representativeness

Candidate sources include public-health, education, civic, media, and approved spoken-transcript subsets. Assess temporal coverage, Haiti/diaspora balance, publisher concentration, translated-text origin, and entity popularity. Do not allow repeated high-frequency entities to dominate the test set.

## Splits and Leakage

Group by source document and provenance unit. Measure entity-string overlap across splits and report memorization-sensitive subsets. Consider source-held-out and temporal challenge sets. Derived transcripts, translations, and normalized versions of one item must remain in one split group.

## Evaluation Candidates

Candidate primary metric: micro exact-match character-span F1 with type. Secondary evidence: macro F1 by entity type, precision, recall, boundary-only F1, type accuracy conditional on matched boundaries, nested-entity performance, and bootstrap confidence intervals grouped by document.

## Baselines

- dictionary/gazetteer baseline with leakage controls;
- multilingual encoder token classifier on a documented flat projection;
- span-classification encoder supporting nested entities;
- zero-shot instruction model with deterministic parsing and failure reporting.

## Error Analysis

Analyze boundary errors, type confusion, nested entities, abbreviations, Haitian institutions, place-name variation, code-switching, OCR/ASR derivation, unseen entities, source/domain transfer, and overlap with training entity strings.

## Pilot Gate

Require reviewed entity definitions and boundaries, a validated annotation tool/export, Unicode code-point offset round-trip tests, pilot agreement, evidence before activating nested annotation, a documented discontinuity rate, privacy review, source authorization, leakage analysis, and independent linguistic/methodological approval.

## Publication Artifacts

- entity taxonomy and decision table;
- corpus/type distribution;
- exact and partial agreement results;
- entity-overlap and source-transfer analysis;
- nested versus flat baseline comparison;
- error taxonomy with release-safe examples.

## Open Questions

- Which nested structures provide enough scientific value for v0.1?
- Should `HEALTH_CONDITION`, `LAW_POLICY`, and `EVENT` remain in the core taxonomy?
- How should aliases and acronym expansions be linked without leaking external knowledge?
- Which privacy classes require redaction or exclusion?

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Proposed canonical character-span NER contract. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Internal AI-assisted audit endorsed character spans but requested ontology and nesting revisions. | NEEDS_REVISION |
| 2026-09-10 | Tightened offsets, contiguous scoring, and nesting activation; resubmitted for external review. | SUBMITTED_TO_REVIEW |
