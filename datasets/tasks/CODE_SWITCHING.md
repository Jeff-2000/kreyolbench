# Token-Level Code-Switching Specification

## Status

Current status: SUBMITTED_TO_REVIEW

Decision: `KB-TASK-CS-001`

Task instance: `kb_lc_token_language_id_v0_1`

Task family / type / variant: language contact / code-switch identification / token language ID

Scope status: PILOT_CANDIDATE for v0.1

Owner: Code-switching working group

Required external review: independent Haitian Creole sociolinguist or code-switching specialist

This specification defines one provisional v0.1 language-contact task. It does not make token language identification the permanent boundary of KreyolBench code-switching research. Future reviewed instances may study utterance composition, switch points, spans, intra-token mixing, borrowing, matrix language, multilingual named entities, diaspora variation, or particular language pairs.

## Purpose and Construct

Measure token-level language identity and language-contact status in Haitian Creole multilingual discourse while keeping language, token function, borrowing, switching, and uncertainty separate. Sentence composition and switch boundaries are derived analyses, not independently annotated gold labels.

## Research Value and Use Cases

- Evaluate multilingual models on Haiti and diaspora language contact.
- Support ASR, search, moderation research, and educational systems without treating French-looking forms as automatically French.
- Study register, source, and domain variation in switching behavior.

## Canonical Contract

```json
{
  "input":{
    "raw_text":"Nou bezwen appointment",
    "tokenization_version":"kb-token-v0.1-candidate.1",
    "tokens":[
      {"token_id":"t1","text":"Nou","start_char":0,"end_char":3},
      {"token_id":"t2","text":"bezwen","start_char":4,"end_char":10},
      {"token_id":"t3","text":"appointment","start_char":11,"end_char":22}
    ]
  },
  "target":{
    "annotations":[
      {"token_id":"t1","language_id":"hat","token_type":"WORD","contact_status":"NONE","uncertainty":"NONE"},
      {"token_id":"t2","language_id":"hat","token_type":"WORD","contact_status":"NONE","uncertainty":"NONE"},
      {"token_id":"t3","language_id":"eng","token_type":"WORD","contact_status":"ACTIVE_SWITCH","uncertainty":"NONE"}
    ]
  }
}
```

Use ISO 639-3 language identifiers. Initial expected languages are `hat`, `fra`, `eng`, and `spa`. Use `mul` for inseparable multilingual material, `und` when linguistic content cannot be assigned reliably, and `zxx` for tokens without linguistic content. Additional registered ISO 639-3 codes may be added with evidence.

## Token Types

Initial types are `WORD`, `NAMED_ENTITY`, `NUMBER`, `PUNCTUATION`, `SYMBOL`, `URL`, and `EMOJI`. A named entity still receives a language ID when evidence supports one; token type must not replace language analysis.

## Contact Status and Uncertainty

- `NONE`: no language-contact category is asserted.
- `ACTIVE_SWITCH`: contextual evidence supports an active switch.
- `ESTABLISHED_BORROWING`: a conventional Haitian Creole borrowing; use `language_id=hat`.
- `MIXED_INTRATOKEN`: inseparable multilingual material; use `language_id=mul`.
- `SHARED_AMBIGUOUS`: a form is shared and context does not justify a single contact analysis.
- `UNCERTAIN`: evidence is insufficient; record an uncertainty reason.

Uncertainty is `NONE`, `AMBIGUOUS_FORM`, `INSUFFICIENT_CONTEXT`, or `TOKENIZATION_UNCERTAIN`. These labels are provisional and require independent Haitian Creole sociolinguistic review.

## Annotation Principles

- Annotate the observed form in context, not its presumed etymology alone.
- Do not label a conventional Haitian Creole borrowing as a switch solely because it resembles French or English.
- Use context, morphology, pronunciation evidence when available, and reviewed borrowing guidance.
- Mark inseparable intra-token mixing as `mul/MIXED_INTRATOKEN`; preserve a note for later morpheme-level research.
- Use `und` for genuine ambiguity rather than forcing agreement.
- Version tokenization because language labels depend on token boundaries.
- Do not infer a named entity's language from spelling history or institutional origin; use contextual evidence or `und`.
- Derive sentence language composition from lexical token labels. Derive switch boundaries only from active contextual switches, excluding borrowings, shared ambiguity, uncertainty, `und`, and `zxx`.

## Inclusion and Exclusion

Include natural multilingual text or transcripts with sufficient context and authorized provenance. Exclude automatically translated or generated multilingual text from principal natural-code-switch claims unless analyzed as a declared stratum. Social-media and private communication require elevated ethics and terms review.

## Annotation and Quality Control

Pilot across formal/informal, Haiti/diaspora, written/spoken, and domain strata where legally available. Independently annotate language ID, token type, contact status, and uncertainty. Report agreement for each factor, ambiguous/borrowing rates, derived-boundary agreement, and adjudication categories. Native Haitian Creole expertise is mandatory.

## Sources and Representativeness

Candidate families include approved radio transcripts, media, diaspora publications, and ethically governed social media. Assess transcription origin, ASR errors, speaker/community representation, French prestige effects, English diaspora effects, Spanish contact, time, and register. Do not claim national dialect coverage without evidence.

## Splits and Leakage

Group by speaker, conversation, episode, thread, document, and provenance unit as applicable. Avoid speaker or near-duplicate leakage. Report source-held-out and register-held-out performance when feasible. Derived transcripts and corrected versions remain in one group.

## Evaluation Candidates

Candidate primary metric: macro F1 across lexical language IDs. Secondary evidence: micro F1, per-language precision/recall/F1, token accuracy, contact-status macro F1, uncertainty and borrowing rates, switch-boundary F1, sentence-composition exact match, performance by token type, and grouped bootstrap confidence intervals. Report results both including and excluding `und`/`mul`; do not collapse contact-status performance into the language-ID score.

## Baselines

- majority and token-frequency lookup baselines using training data only;
- character n-gram language identifier;
- multilingual contextual token classifier;
- sequence model with contextual constraints;
- zero-shot instruction model with deterministic token alignment checks.

## Error Analysis

Analyze borrowing versus switching, cognates, named entities, clitics, intra-token mixing, punctuation adjacency, tokenization, ASR errors, Haiti/diaspora differences, speaker/source transfer, and rare languages.

## Pilot Gate

Require reviewed borrowing and ambiguity rules, versioned tokenization, pilot agreement, speaker/document grouping, elevated review for sensitive sources, tested derived-boundary logic, metric definitions, and independent sociolinguistic approval.

## Publication Artifacts

- language/contact taxonomy;
- source/register composition;
- per-language and borrowing agreement;
- switch-pattern and boundary analysis;
- baseline results by source and token type;
- release-safe qualitative error examples.

## Open Questions

- Which established borrowings belong to Haitian Creole for this protocol?
- When is a named entity language-identifiable rather than `und`?
- Is morpheme-level annotation necessary for a later release?
- Which spoken and diaspora strata can be represented without overclaiming?

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-09 | Replaced BIO language tags with direct token-level language IDs. | SUBMITTED_TO_REVIEW |
| 2026-09-10 | Internal AI-assisted audit requested a borrowing-aware factorized contact ontology. | NEEDS_REVISION |
| 2026-09-10 | Added token offsets, contact status, uncertainty, and derived-boundary rules; resubmitted for external review. | SUBMITTED_TO_REVIEW |
