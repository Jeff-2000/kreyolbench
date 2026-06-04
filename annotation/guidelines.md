# KreyolBench Annotation Guidelines

Annotate what is present in the text. Preserve raw Kreyol spelling unless the task is normalization. Mark uncertainty rather than guessing.

## Topic Classification

Choose one label: `health`, `education`, `civic_admin`, `disaster_response`, `economy`, `security`, `culture`, `religion`, or `other`.

Example: `Lave men nou ak savon pou evite kolera.` -> `health`.

## Named Entity Recognition

Use BIO tags. Entity types: `PER`, `ORG`, `LOC`, `GPE`, `DATE`, `TIME`, `MONEY`, `PERCENT`, `FACILITY`, `HEALTH_CONDITION`, `PRODUCT`, `LAW_POLICY`, `EVENT`.

Example: `MSPP anonse yon kanpay vaksinasyon nan Pòtoprens lendi.`
`MSPP/ORG`, `Pòtoprens/GPE`, `lendi/DATE`.

## Question Answering

Answers must be exact spans copied from the context. If no answer is present, set `is_unanswerable=true` and leave answer text empty.

Example: Context `Biwo a ouvri lendi rive vandredi.` Question `Ki jou biwo a ouvri?` Answer `lendi rive vandredi`.

## Retrieval

Judge query-document relevance: `0` not relevant, `1` related, `2` relevant, `3` highly relevant.

## Normalization

Keep `raw_text` unchanged. Write standard Kreyol in `normalized_text`. Record edit types such as `standardize_spelling`, `split_merge`, `apostrophe`, `accent`, `punctuation`, or `no_change`.

Example: raw `m pa konn si lap vini` -> normalized `mwen pa konnen si l ap vini`.

## Code-Switching

Sentence labels: `hat`, `hat-fra`, `hat-eng`, `hat-spa`, `mixed-other`, `unknown`.
Token labels: `B-HAT`, `I-HAT`, `B-FRA`, `I-FRA`, `B-ENG`, `I-ENG`, `B-SPA`, `I-SPA`, `PUNCT`, `NUM`, `OTHER`.

Example: `Nou bezwen appointment pou sèvis la.` -> sentence `hat-eng`, token `appointment=B-ENG`.

## Quality Control

Use a 10% gold set, double annotate 20-30% of v0, adjudicate disagreements, and report agreement metrics by task.

