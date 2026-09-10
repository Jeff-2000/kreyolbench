# Orthography-Only Normalization Specification

## Status

Current status: SUBMITTED_TO_REVIEW

Decision: `KB-TASK-NORM-001`

Task instance: `kb_norm_orthography_v0_1`

Task family / type / variant: normalization / orthographic normalization / multi-reference orthography-only

Scope status: PILOT_CANDIDATE for v0.1

Owner: Normalization working group

Required external review: independent Haitian Creole linguist or orthography specialist

This specification defines one deliberately narrow v0.1 task instance. It does not define normalization globally. OCR correction, ASR transcript normalization, historical spelling, noisy social text, and other future constructs require separate specifications and must not be collapsed into this task. Capitalization and punctuation are retained only as separately tagged auxiliary strata and are excluded from the candidate primary score pending external review.

## Purpose and Construct

Measure conversion of a Haitian Creole surface form into one or more accepted orthographic forms while preserving meaning, lexical choice, grammar, register, and code-switching. The task is not translation, paraphrasing, grammatical correction, or formalization.

## Research Value and Use Cases

- Improve search, educational tools, and text processing without erasing raw variation.
- Quantify model behavior across spacing, apostrophe, accent, and spelling variation.
- Create an explicit test of normalization uncertainty and legitimate alternatives.

## Canonical Contract

```json
{
  "input":{"raw_text":"M pa konnen si lap vini"},
  "target":{
    "decision":"ERROR_CORRECTION",
    "references":["M pa konnen si l ap vini"],
    "edits":[{"type":"spacing","evaluation_stratum":"CORE","rule_id":"KB-ORTH-CAND-002","raw_start":15,"raw_end":18,"raw":"lap","replacement":"l ap"}]
  }
}
```

Raw text is immutable. References may contain multiple accepted forms. Every changed region requires a typed edit record, `CORE` or `AUXILIARY` evaluation stratum, normative `rule_id`, and transformation provenance. `ABSTAIN` rows have no references or edits and are excluded from scoring.

## Allowed Changes

- `spacing`: merge or split tokens according to an accepted orthographic rule;
- `apostrophe`: add, remove, or standardize apostrophe use;
- `spelling_convention`: change spelling without substituting a different lexical item;
- `accent`: correct or standardize diacritics;
- `capitalization`: alter case where the chosen protocol requires it;
- `punctuation`: alter punctuation without changing propositional meaning.

Core candidate transformations are spacing, apostrophe, spelling convention, and accent/diacritic edits. Capitalization and punctuation are auxiliary strata and cannot affect the candidate primary score. Unicode and typographic cleanup are deterministic preprocessing operations, not gold linguistic edits.

## Decision Classes and Normative Evidence

- `ERROR_CORRECTION`: the observed form conflicts with a documented reviewed rule.
- `ACCEPTABLE_VARIANT_NORMALIZATION`: a permitted target form is selected without claiming the observed form is erroneous.
- `ACCEPT_AS_IS`: no supported linguistic edit is warranted; the sole reference equals raw text.
- `ABSTAIN`: available evidence cannot support a responsible target; the row is not scored.

Every edit references `configs/orthography/normative_evidence.yaml`. A scholarly discussion, institutional publication, or frequent attestation is not automatically a normative rule. Unknown authority remains `TO_VERIFY`; annotator intuition cannot fill the gap.

## Prohibited Changes

- lexical expansion or substitution, such as changing `m` to `mwen` or `konn` to `konnen`;
- translation or replacement of a code-switched expression;
- grammatical rewriting or inferred correction;
- formalization, register conversion, stylistic editing, or censorship;
- removal of dialectal evidence merely to simplify modeling.

If an item cannot be normalized without a prohibited change, mark it `NO_ORTHOGRAPHIC_DECISION` or exclude it under a reviewed rule rather than rewriting it.

## Annotation Protocol

1. Preserve raw text and context.
2. Decide whether an orthographic change is warranted under a cited guideline.
3. Produce every materially acceptable reviewed reference within the task scope.
4. Record each edit type, evaluation stratum, raw offset, decision class, and normative rule ID.
5. Flag ambiguity, code-switch interaction, uncertain lexical identity, and guideline gaps.
6. Adjudicate repeated ambiguity and update the rule inventory with version history.

## Sources and Representativeness

AKA materials may guide orthographic review but are not automatically corpus data. Candidate examples may eventually come from approved speech transcripts, media, diaspora, or ethically governed informal-text subsets. Analyze register, region, time, authoring origin, ASR/OCR effects, and the degree to which collection methods overproduce nonstandard forms.

## Splits and Leakage

Group the same raw item, near duplicates, alternate references, and derivatives in one split. Hold out transformation patterns or sources for robustness only when sample sizes support interpretation. Prevent normalization dictionaries derived from test references from entering training.

## Evaluation Candidates

Candidate primary metric: exact match against any accepted reference using core edits only. Capitalization and punctuation receive separate auxiliary reporting. Secondary evidence: character error rate to the closest reference, word-level accuracy, edit precision/recall/F-score by type, unchanged-case accuracy, over-normalization rate, abstention coverage, and bootstrap confidence intervals grouped by source unit. Exact match alone is insufficient.

## Baselines

- identity/no-change baseline;
- reviewed rule-based normalizer;
- character-level sequence model;
- multilingual encoder-decoder with constrained decoding;
- retrieval or lexicon-assisted approach using training-only resources.

## Error Analysis

Analyze edit type, over-normalization, under-normalization, legitimate alternate forms, code-switching, named entities, clitics, punctuation, ASR/OCR derivation, register, source transfer, and semantic changes introduced by a system.

## Pilot Gate

Require reviewed boundaries between orthography and lexical choice, a versioned rule inventory, multiple-reference policy, pilot agreement by edit type, transformation provenance, semantic-preservation review, source authorization, tested metrics, and independent linguistic approval.

## Publication Artifacts

- transformation taxonomy and rule table;
- edit-type and ambiguity distributions;
- annotator agreement by edit type;
- identity/rule/model baseline comparison;
- over-normalization and semantic-preservation analysis;
- source/register robustness table.

## Open Questions

- Which capitalization and punctuation rules belong in the primary score?
- How many accepted alternatives can be represented reliably?
- How should fused forms with competing linguistic analyses be handled?
- Which reference authority or authorities govern each rule version?

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Narrowed the task to orthographic transformations and multiple references. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Internal AI-assisted audit requested stronger linguistic boundaries and normative grounding. | NEEDS_REVISION |
| 2026-09-10 | Separated core/auxiliary edits and added decision classes and evidence requirements; resubmitted for external review. | SUBMITTED_TO_REVIEW |
