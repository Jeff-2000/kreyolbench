# v0.1 Candidate Named-Entity Ontology

## Purpose

Define the reviewable entity-type and boundary contract for `kb_ie_ner_charspan_v0_1`. The machine-readable candidate inventory is `configs/labels/ner.yaml`.

## Status

Current status: SUBMITTED_TO_REVIEW

Decision: `KB-TASK-NER-001`

Ontology version: `ner-v0.1-candidate.2`

## Canonical Representation

- Gold annotations reference immutable raw text.
- Offsets are zero-based, end-exclusive Unicode code-point indexes.
- v0.1 scored mentions are contiguous spans.
- BIO/BILOU views are derived, tokenization-versioned exports.
- Crossing spans are prohibited.
- Nesting is representable but disabled in routine pilot annotation until pilot evidence and external approval justify it.
- Discontinuous candidates are flagged as unsupported pilot cases and excluded from scoring without deleting their source context.

## Candidate Types

| Type | Candidate construct | Key confusion requiring review |
| --- | --- | --- |
| `PER` | named individual or explicitly named person-like referent | titles and unnamed roles |
| `ORG` | named organization, agency, company, association, or institution | facilities and metonymic locations |
| `LOC` | physical geographic feature or non-administrative place | geopolitical or administrative units |
| `GPE` | country, department, commune, city, or other geopolitical unit | locations used only as sites |
| `FACILITY` | named building, hospital, school site, road, port, or physical facility | organization operating at that site |
| `EVENT` | named event, disaster, election, campaign, or historically bounded occurrence | generic event descriptions |
| `DATE` | calendrical expression | durations and vague time references |
| `TIME` | clock time or bounded time-of-day expression | dates and durations |
| `MONEY` | monetary value with explicit or recoverable currency | bare quantities |
| `PERCENT` | percentage or rate expression | unrelated decimal quantities |
| `PRODUCT` | named product, medicine, platform, or artifact | generic object classes |
| `HEALTH_CONDITION` | named disease, syndrome, or reviewed clinical condition | generic symptoms or unreviewed inferred diagnoses |
| `LAW_POLICY` | named law, decree, policy, program, or formal public measure | generic legal or administrative discussion |

This list is provisional. A richer Haitian institutional ontology is scientifically attractive but must not be added without pilot prevalence and annotation-burden evidence.

## Boundary Principles

- Include the minimal complete referring expression supported by the ontology.
- Handle titles, honorifics, determiners, acronyms, coordinated entities, possessives, and aliases through explicit reviewed examples.
- Record acronyms independently when they form a complete named mention; do not infer hidden long forms.
- Type metonymic uses by contextual referent, with ambiguity flagged for adjudication.
- Do not infer a person's sensitive attributes from names or contextual stereotypes.
- Publicly release no unnecessary PII merely because it can be tagged as an entity.

## Pilot Evidence Required

- Positive, negative, and boundary counterexamples for every type.
- Type-confusion matrix and adjudication log.
- Exact-span/type agreement and relaxed boundary diagnostics.
- Prevalence and source-domain distribution by type.
- Review of nesting and discontinuity frequency before either is activated.
- Entity-family grouping plan for split leakage prevention.

## Open Questions

- Is `LAW_POLICY` reliable and sufficiently frequent?
- Can annotators consistently distinguish `ORG` from `FACILITY` and `LOC` from `GPE`?
- Which Haitian administrative and institutional names create recurrent metonymy?
- Does any source justify nested annotation strongly enough to offset its cost?

## Acceptance Criteria

- Qualified external review covers Haitian Creole linguistics and NER methodology.
- Pilot evidence supports the ontology, boundaries, and annotation burden.
- Character-span validity tests pass on raw Unicode text.
- Entity and source grouping rules prevent obvious leakage.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-10 | Added the candidate type ontology, offset contract, boundary questions, and pilot evidence gates. | SUBMITTED_TO_REVIEW |
