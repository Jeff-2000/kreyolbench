# Internal Scientific Audit of the v0.1 Task Specifications

## Purpose

Record the pre-external-review scientific audit of the five KreyolBench v0.1 pilot candidates and the corrections required before independent review.

## Status

Current status: TO_REVIEW_LATER

Audit date: 2026-09-10

Adopted by: Jeff Pierre, Project Lead and Scientific Reviewer

Review independence: INTERNAL_PROJECT_LEAD

AI assistance: The analysis and drafting were AI-assisted. Jeff Pierre reviewed and adopted the revision disposition. This record is not an external human review and cannot satisfy `KB-GOV-002` or `KB-GOV-003`.

## Scope and Disposition

All five task directions remain scientifically promising and remain `PILOT_CANDIDATE`. Their specifications required correction before identifiable external experts should be asked to approve them.

| Decision | Internal outcome | Main revision requirement | Post-revision status |
| --- | --- | --- | --- |
| `KB-TASK-CLS-001` | REVISED | Define and pilot a versioned multi-label topic ontology and suitable agreement analysis. | `SUBMITTED_TO_REVIEW` |
| `KB-TASK-NER-001` | REVISED | Freeze offset semantics and a versioned entity ontology; limit scored pilot mentions to contiguous spans. | `SUBMITTED_TO_REVIEW` |
| `KB-TASK-RET-001` | REVISED | Operationalize query provenance, pooling, qrels, unjudged-document treatment, and temporal validity. | `SUBMITTED_TO_REVIEW` |
| `KB-TASK-NORM-001` | REVISED | Ground orthography-only edits in explicit normative evidence and separate auxiliary surface strata. | `SUBMITTED_TO_REVIEW` |
| `KB-TASK-CS-001` | REVISED | Factor language identity from contact status and specify borrowing, ambiguity, tokenization, and entities. | `SUBMITTED_TO_REVIEW` |

`REVISED` is a review-event outcome. The decisions briefly entered `NEEDS_REVISION` conceptually while the accepted changes were implemented and now return to `SUBMITTED_TO_REVIEW`. No external approval has been recorded.

## Classification Findings

Retain multi-label topic classification and keep topic distinct from domain, genre, register, source, and audience. Before freeze, the ontology must define every label, positive and negative boundaries, permissible co-occurrences, uncertainty, rare-label handling, and the mutually exclusive `other` class. Agreement analysis must include per-label binary summaries, set-based precision/recall/F1, and a justified bootstrapped chance-adjusted multi-label analysis; ordinary Cohen's kappa alone is insufficient. Model threshold selection belongs to evaluation and must use validation data only.

Evidence: Marchal et al. show why multi-label agreement requires methods designed for set-valued annotations rather than uncritical reuse of single-label agreement measures: <https://aclanthology.org/2022.coling-1.322/>.

## Named-Entity Recognition Findings

Retain immutable raw text with zero-based, end-exclusive Unicode code-point offsets as the canonical representation. BIO/BILOU are derived exports. The schema may represent nesting, but routine v0.1 annotation keeps nesting disabled until pilot evidence and external approval justify it. Scored mentions are contiguous; discontinuous candidates are retained as source evidence but excluded from pilot scoring. A versioned entity ontology and detailed boundary policy remain mandatory.

Span-oriented NER research supports decoupling entity prediction from a single BIO sequence representation, but it does not by itself validate KreyolBench's exact offset or ontology policy. Those are project design choices still requiring external review: <https://aclanthology.org/2021.acl-long.558/>.

## Retrieval Findings

Retain separate corpus, query, and qrels artifacts. Query origin must be explicit, and document-derived diagnostic queries cannot enter the principal test set. Missing qrels mean `UNJUDGED`, not canonical relevance zero. Evaluation must explicitly document how each metric treats unjudged documents and report judgment coverage. Candidate pooling must include lexical, character n-gram, multilingual dense, and reranking systems, with pooling-depth sensitivity analysis.

Evidence: TREC methodology separates collections, topics, system pools, and relevance judgments (<https://trec.nist.gov/howto.html>). Standard `trec_eval` behavior and measure definitions must be made explicit (<https://github.com/usnistgov/trec_eval>). Pool incompleteness can bias evaluation (<https://www.nist.gov/publications/bias-and-limits-pooling-large-collections>).

## Normalization Findings

Retain an orthography-focused construct, but distinguish core spelling, spacing, apostrophe, and diacritic edits from auxiliary capitalization and punctuation strata. Unicode and typographic cleanup are deterministic preprocessing, not gold linguistic normalization. Every linguistic transformation requires versioned normative evidence. Decisions must distinguish error correction, acceptable-variant normalization, accept-as-is, and abstention. Multiple acceptable references are required where justified.

Haitian Creole orthographic standardization includes variation and sociolinguistic consequences; it cannot be reduced to intuitive spelling correction. Contextual background includes Valdman (<https://scholarworks.iu.edu/dspace/items/f9ef342f-c1cc-40bc-b29f-747985df5eed>) and Schieffelin and Doucet (<https://anthrosource.onlinelibrary.wiley.com/doi/10.1525/ae.1994.21.1.02a00090>). These works are contextual evidence, not automatic authority for individual gold edits.

## Code-Switching Findings

Retain token-level language identification but factor it from token type, contact status, and uncertainty. Established Haitian Creole borrowings use `hat` with `ESTABLISHED_BORROWING`; etymological resemblance alone cannot produce a French or English label. Named entities require contextual policy. Tokenization is versioned and character-linked. Derived switch boundaries include active contextual transitions and exclude punctuation, borrowing, `und`, and `zxx`.

Borrowing and code-switching require dedicated treatment rather than language ID alone: <https://aclanthology.org/2022.lrec-1.342/>. The Radio Haiti-Inter corpus demonstrates research relevance for spoken language contact, but neither its paper nor its existence establishes KreyolBench access or redistribution rights: <https://aclanthology.org/2026.lrec-1.241/>.

## Cross-Task Requirements Before Validation

- At least one identifiable external independent human approval per task.
- Collectively documented expertise matching the task-specific requirements.
- Reviewer affiliation and conflict disclosure.
- Dated evidence stored under `reports/reviews/`.
- Pilot evidence for ontology coverage, annotation reliability, ambiguity, and workload.
- Source-specific legal, ethical, provenance, and scientific authorization.
- No task freeze based only on this internal audit.

## Known Limitations

- No real source content was inspected or collected for this audit.
- No pilot annotations or empirical agreement estimates exist.
- Candidate labels and rules remain provisional.
- Cited literature supports the concerns and methodological direction; it does not validate the final Haitian Creole task constructs.

## Acceptance Criteria

- The five specifications incorporate every accepted correction.
- Machine-readable task contracts and synthetic fixtures match the specifications.
- Decision histories retain this internal `REVISED` event.
- All five decisions remain `SUBMITTED_TO_REVIEW` until qualified external evidence is recorded.

## Next Recommended Action

Recruit identifiable external reviewers using `reports/TASK_SPEC_REVIEW_PACKET_V0_1.md` and the templates in `reports/reviews/`. In parallel, perform metadata-only source feasibility assessments. Do not collect source content or start annotation.

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-10 | Recorded the AI-assisted internal project-lead audit and adopted pre-external-review corrections. | TO_REVIEW_LATER |
