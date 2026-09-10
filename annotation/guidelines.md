# KreyolBench Annotation Guidelines

Annotate what is present in the text. Preserve raw Kreyol spelling unless the task is normalization. Mark uncertainty rather than guessing.

## Topic Classification

Choose every substantively applicable topic from `health`, `education`, `civic_admin`, `disaster_response`, `economy`, `security`, `culture`, `religion`, or `other`, using the versioned ontology in `configs/labels/topic.yaml`. `other` is exclusive and requires a taxonomy-gap justification. Do not use source, audience, domain, genre, or register as topic labels. Record label-level uncertainty rather than resolving ambiguity by intuition.

Example: `Lave men nou ak savon pou evite kolera.` -> `[health]`.

## Named Entity Recognition

Annotate typed, zero-based, end-exclusive Unicode code-point spans over immutable raw text. v0.1 scored spans are contiguous. The schema can represent nesting, but routine nested annotation is disabled until pilot evidence and external approval activate it. Crossing spans are prohibited. Flag discontinuous mentions for adjudication and exclude them from v0.1 scoring without erasing the source case. BIO/BILOU tags may be generated only as versioned derived exports. Candidate entity types are `PER`, `ORG`, `LOC`, `GPE`, `DATE`, `TIME`, `MONEY`, `PERCENT`, `FACILITY`, `HEALTH_CONDITION`, `PRODUCT`, `LAW_POLICY`, and `EVENT`.

Example: `MSPP anonse yon kanpay vaksinasyon nan Pòtoprens lendi.` contains `MSPP/ORG` at `[0,4)`, `Pòtoprens/GPE` at `[39,48)`, and `lendi/DATE` at `[49,54)`.

## Question Answering

Answers must be exact spans copied from the context. If no answer is present, set `is_unanswerable=true` and leave answer text empty.

Example: Context `Biwo a ouvri lendi rive vandredi.` Question `Ki jou biwo a ouvri?` Answer `lendi rive vandredi`.

## Retrieval

Judge query-document usefulness for the stated information need: `0` not useful, `1` related but insufficient, `2` substantively useful but incomplete, and `3` directly useful. Missing qrels mean `UNJUDGED`, not relevance zero. Standard metrics may treat unjudged documents as nonrelevant computationally; report that treatment, `judged@k`, `bpref`, and pooling sensitivity separately. Corpus, query, and qrel records are stored separately. Document-derived diagnostic queries may not enter principal test splits.

## Normalization

Keep `raw_text` unchanged. Classify the item as `ERROR_CORRECTION`, `ACCEPTABLE_VARIANT_NORMALIZATION`, `ACCEPT_AS_IS`, or `ABSTAIN`. Core v0.1 edits are spacing, apostrophes, spelling conventions, and diacritics. Capitalization and punctuation are separately tagged auxiliary strata and do not enter the candidate primary score. Unicode or typographic cleanup belongs to deterministic preprocessing, not gold linguistic normalization. Every edit requires a versioned normative `rule_id`. Do not perform lexical substitution, translation, grammatical rewriting, or register conversion.

Example: raw `M pa konnen si lap vini` -> reference `M pa konnen si l ap vini`. Changing `m` to `mwen` or `konn` to `konnen` is outside this task.

## Code-Switching

Tokenize immutable raw text with a versioned policy and preserve every token's character offsets. For each token, annotate `language_id`, `token_type`, `contact_status`, and uncertainty. Contact status is provisionally one of `NONE`, `ACTIVE_SWITCH`, `ESTABLISHED_BORROWING`, `MIXED_INTRATOKEN`, `SHARED_AMBIGUOUS`, or `UNCERTAIN`. Established Haitian Creole borrowings use `hat`; etymological similarity alone never makes a token French or English. Use `mul` only for inseparable mixed forms, `und` for unresolved assignment, and `zxx` for non-linguistic material. Derive switch boundaries from active contextual switches, excluding borrowings, ambiguity, punctuation, `und`, and `zxx`.

Example: in `Nou bezwen appointment`, `appointment` may be `eng/WORD/ACTIVE_SWITCH` only when context supports active switching; a conventional borrowing would instead be `hat/WORD/ESTABLISHED_BORROWING`.

## Quality Control

Pilot each task, define a task-specific double-annotation proportion and calibration set from evidence, adjudicate disagreements, and report appropriate agreement measures. No universal percentage or agreement threshold is frozen.
