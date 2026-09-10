# v0.1 Candidate Topic Ontology

## Purpose

Define the reviewable semantic contract for `kb_cls_topic_multilabel_v0_1`. The machine-readable authority is `configs/labels/topic.yaml`; this document explains how the candidate labels must be tested before freeze.

## Status

Current status: SUBMITTED_TO_REVIEW

Decision: `KB-TASK-CLS-001`

Ontology version: `topic-v0.1-candidate.2`

The scoring ontology is flat. Any conceptual relationships are provisional metadata and do not change scoring.

## Construct Boundaries

Topics describe what an item substantively concerns. They must not encode publisher, source institution, genre, register, audience, or collection domain. For example, an MSPP document is not automatically `health`, and a government document is not automatically `civic_admin`; the text must support the topic.

| Label | Positive boundary | Negative boundary |
| --- | --- | --- |
| `health` | health conditions, care, prevention, health services, or public-health action | institutional provenance without substantive health content |
| `education` | teaching, learning, schools, curricula, literacy, access, or educational policy | any text merely written for students |
| `civic_admin` | public services, rights, duties, elections, administration, laws, or official procedures | any text published by government |
| `disaster_response` | preparedness, alerts, hazards, emergency response, relief, or recovery | hardship without a hazard or response construct |
| `economy` | work, trade, prices, income, finance, production, or livelihoods | incidental monetary amounts without economic substance |
| `security` | public safety, violence prevention, policing, justice, or personal security | safety advice better represented by health or disaster response alone |
| `culture` | arts, heritage, language, identity, customs, or cultural production | language of publication alone |
| `religion` | faith, worship, doctrine, religious institutions, or practice | moral language without a religious construct |
| `other` | a coherent substantive topic not represented above | uncertainty, missing context, or a second label alongside a listed topic |

Detailed inclusion and exclusion examples remain in `configs/labels/topic.yaml`. Pilot examples must be expanded by independent domain review; synthetic examples are not evidence of coverage.

## Multi-Label Rules

- Apply every substantively supported label; do not force one dominant topic.
- Co-occurrence is allowed between substantive labels when each independently satisfies its definition.
- `other` is mutually exclusive and requires a taxonomy-gap justification.
- Use `UNCERTAIN` when evidence for one or more candidate labels is ambiguous.
- Use `MISSING_CONTEXT` when the available unit cannot support a defensible decision.
- Do not use `other` as an uncertainty label.

## Pilot Evidence Required

- Positive and negative boundary examples for every label.
- Co-occurrence matrix and review of implausible combinations.
- Prevalence and effective sample size per label.
- Taxonomy-gap analysis from `other` justifications.
- Per-label binary agreement and disagreement analysis.
- Set-based annotator precision, recall, and F1.
- A preregistered bootstrapped chance-adjusted multi-label agreement analysis.
- Rare-label uncertainty intervals and a merge/defer rule.

## Evaluation Boundary

Gold semantics do not depend on a model threshold. Fixed thresholds and validation-tuned thresholds must be reported separately. Tuning on a test split is prohibited.

## Open Questions

- Are the candidate labels meaningful across civic, health, education, media, and diaspora registers?
- Does `civic_admin` remain coherent, or should future evidence separate rights, law, elections, and services?
- Which co-occurrences are real rather than artifacts of long documents?
- What minimum prevalence supports stable per-label claims?

## Acceptance Criteria

- Qualified external expertise covers Haitian Creole domain knowledge and multi-label classification.
- Pilot evidence supports label boundaries and annotator reliability.
- Every ontology change increments the version and preserves revision rationale.
- The task remains `SUBMITTED_TO_REVIEW` until those conditions are met.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-10 | Added the flat candidate ontology, construct boundaries, and pilot validation requirements. | SUBMITTED_TO_REVIEW |
