# Decision Register

## Purpose

Track important scientific and architectural decisions using stable identifiers.

## Status

Current status: IN_PROGRESS

Owner: Codex

Requires expert validation: Yes for scientific decisions.

## Decision Format

```text
ID:
Title:
Date:
Status:
Context:
Decision:
Alternatives considered:
Scientific rationale:
Engineering implications:
Risks:
Requires expert approval:
Expert decision:
Review history:
```

## KB-DEC-001

Title: Project-wide review-status policy

Date: 2026-09-01

Status: EXPERT_VALIDATED

Context: KreyolBench needs durable expert review gates across scientific artifacts and implementation work.

Decision: Use `DRAFT`, `IN_PROGRESS`, `TO_REVIEW_LATER`, `SUBMITTED_TO_REVIEW`, `EXPERT_VALIDATED`, `NEEDS_REVISION`, `BLOCKED`, and `DEPRECATED` across major knowledge files, task specs, metrics, source review, paper sections, and releases.

Alternatives considered: informal TODOs only; GitHub issue labels only; no status model.

Scientific rationale: benchmark validity depends on distinguishing provisional scaffold decisions from expert-validated decisions.

Engineering implications: Markdown files should include status blocks; future schemas may encode status fields.

Risks: too much blocking could slow engineering; too little blocking could create unsupported scientific claims.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-08, subject to the conditions recorded in `reports/EXPERT_REVIEW_PACKET_V0_1.md`.

## KB-DATA-001

Title: Multi-axis source registry and release authorization gate

Date: 2026-09-01

Status: EXPERT_VALIDATED

Context: Candidate sources exist, but discovery, access, collection, derived use, redistribution, ethics, and scientific inclusion are independent questions. A single source-review status cannot represent these gates safely.

Decision: Every committed source record must use source schema version 2 and independently record discovery, access, legal review, collection authorization, derived-use authorization, redistribution, commercial use, ethics, and scientific inclusion. Public availability or collection approval does not imply permission for another use. Public release requires explicit source-specific evidence and all applicable gates.

Alternatives considered: retain one overloaded `review_status`; commit public web text directly; infer redistribution from accessibility; rely on README source lists only.

Scientific rationale: provenance and legal clarity are required for credible dataset releases.

Engineering implications: source configs use typed, multi-axis governance metadata. Audits validate hierarchy, incompatible permissions, evidence, and release gates. Broad source families cannot back dataset rows.

Risks: source review may delay dataset growth; duplicated state may drift; conditional rights may be interpreted too broadly.

Requires expert approval: Yes

Expert decision: Revision requested by Jeff Pierre on 2026-09-08. The revised policy was approved by Jeff Pierre on 2026-09-09 at project-policy level. This approval authorizes source-specific feasibility review only; it does not authorize acquisition, transformation, annotation, redistribution, scientific inclusion, or release for any source.

Review history:

- 2026-09-08, `REVISED`, internal project-lead review; evidence: `reports/EXPERT_REVIEW_PACKET_V0_1.md`.
- 2026-09-09, `APPROVED`, internal project-lead review; evidence: `reports/EXPERT_REVIEW_PACKET_V0_1.md`.

## KB-DATA-002

Title: Raw and normalized text preservation policy

Date: 2026-09-01

Status: EXPERT_VALIDATED

Context: Haitian Creole orthographic variation is scientifically meaningful but normalization may be useful for evaluation.

Decision: Preserve raw text whenever normalized text is created; normalization must not overwrite or erase raw forms.

Alternatives considered: normalize all text early; avoid normalization entirely.

Scientific rationale: raw forms support analysis of spelling variation, register, and domain differences.

Engineering implications: schemas and preprocessing should maintain raw-to-normalized linkage.

Risks: storage and annotation complexity increase.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-08 with mandatory transformation provenance and linguistic-review conditions.

## KB-DATA-003

Title: Open-world source discovery and corpus expansion policy

Date: 2026-09-09

Status: EXPERT_VALIDATED

Context: Haitian Creole resources are distributed across institutions, archives, research releases, public agencies, publishers, and communities. A fixed source whitelist would become incomplete and could discourage scientifically valuable discovery.

Decision: KreyolBench maintains an open-world source discovery process. New source families, collections, and subsets may be registered continuously. Registration authorizes metadata discovery only and never implies authorization for collection, annotation, transformation, redistribution, commercial use, benchmark inclusion, or publication claims.

Alternatives considered: freeze a permanent whitelist; allow only preapproved providers; treat registration as provisional collection approval.

Scientific rationale: an extensible registry supports corpus diversity, temporal coverage, new research releases, and community contributions while preserving independent scientific-quality review.

Engineering implications: source records support parent-child hierarchy and discovery-only families. Each downstream action is controlled by its own machine-readable gate.

Risks: collaborators may misread discovery as endorsement; registry growth may create duplicated or low-value entries.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-09. Source-specific approvals remain separate and pending unless explicitly recorded.

## KB-ANN-001

Title: Annotation quality-control policy

Date: 2026-09-01

Status: EXPERT_VALIDATED

Context: Existing annotation guidelines mention gold sets, double annotation, adjudication, and agreement reporting.

Decision: Annotation campaigns require pilot review, gold examples, double annotation of a defined subset, adjudication, agreement reporting, and uncertainty labels where appropriate.

Alternatives considered: single annotation only; informal review after annotation.

Scientific rationale: benchmark reliability depends on annotator agreement and transparent disagreement handling.

Engineering implications: annotation exports must preserve annotator/adjudication metadata privately.

Risks: annotation cost and coordination burden increase.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-08. Task-specific agreement measures, thresholds, and double-annotation proportions remain subject to pilot evidence and separate review.

## KB-EVAL-001

Title: Metric and statistical-testing policy

Date: 2026-09-01

Status: EXPERT_VALIDATED

Context: Current metric implementations are scaffold-level for several tasks.

Decision: Every metric must document definition, averaging, limitations, uncertainty method, and appropriateness. Leaderboards must not interpret small differences as meaningful without uncertainty or significance analysis.

Alternatives considered: rank by one aggregate score only; report point estimates only.

Scientific rationale: low-resource benchmarks are sensitive to small samples, imbalance, and domain effects.

Engineering implications: result JSON should eventually include confidence intervals and run metadata.

Risks: statistical testing may be misused if sample sizes are too small.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-08 at policy level. Task-level metric matrices remain provisional.

## KB-SPLIT-001

Title: Split, leakage, and contamination policy

Date: 2026-09-01

Status: EXPERT_VALIDATED

Context: Train/validation/test split names exist, but split logic and contamination policy are not yet formalized.

Decision: Dataset splits require stable IDs, hashing, source-aware grouping, duplicate checks, and test contamination review before release.

Alternatives considered: random row-level splits only.

Scientific rationale: leakage can invalidate benchmark claims.

Engineering implications: future validators should check duplicate IDs, source overlap, and near-duplicate contamination.

Risks: strict grouping may reduce split size.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-09. No universal split ratio or near-duplicate threshold was approved.

## KB-PUB-001

Title: Publication artifact traceability policy

Date: 2026-09-01

Status: EXPERT_VALIDATED

Context: The paper outline needs to evolve with implementation artifacts.

Decision: Tables, figures, datasets, metrics, and experiments intended for publication must be linked to paper sections with status, evidence requirements, and implementation dependencies.

Alternatives considered: write paper after implementation from memory.

Scientific rationale: traceability reduces publication drift and unsupported claims.

Engineering implications: reports and results should reference artifact IDs where practical.

Risks: documentation overhead.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-08 with independent reproduction required for material claims whenever practicable.

## KB-SCOPE-001

Title: KreyolBench v0.1 scientific pilot task scope

Date: 2026-09-08

Status: EXPERT_VALIDATED

Context: The seven-task candidate list exceeded a defensible first-release scope for a small research team and risked delaying signature Haitian Creole contributions.

Decision: Retain classification, named entity recognition, retrieval, normalization, and code-switching in the v0.1 scientific pilot. Keep question answering as feasibility work only. Defer translation from the core v0.1 release while preserving it in the architecture. Keep sentiment and summarization on the longer-term roadmap.

Alternatives considered: freeze all seven candidate tasks; reduce v0.1 to conventional classification tasks; remove deferred tasks from the architecture.

Scientific rationale: the five-task pilot balances feasibility, real-world utility, annotation burden, and Haitian-specific scientific value. Normalization and code-switching may become signature contributions.

Engineering implications: the v0.1 release registry must reflect the five-task pilot without treating it as the global task universe. Task schemas, labels, metrics, and dataset inclusion remain independently provisional.

Risks: a five-task pilot may still exceed available annotation capacity; deferral may be misread as permanent exclusion.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-08 through the cross-cutting scope review.

## KB-SCOPE-002

Title: Open-world task and benchmark expansion policy

Date: 2026-09-09

Status: EXPERT_VALIDATED

Context: The first controlled pilot contains five task instances, but task-specific v0.1 choices could be misread as permanent definitions of KreyolBench or its task families.

Decision: KreyolBench maintains an open-world scientific architecture in which task families, task types, variants, instances, domains, modalities, challenge sets, datasets, and evaluation paradigms may be registered when scientifically justified. Registration or roadmap inclusion does not imply scientific validation, implementation priority, release inclusion, data or annotation authorization, metric approval, or publication evidence. Every release remains bounded by explicit membership and applicable governance gates.

Alternatives considered: treat the v0.1 task list as the complete benchmark; enumerate a fixed permanent task universe; add future tasks directly to v0.1.

Scientific rationale: bounded releases preserve validity and feasibility, while an open-world program prevents early implementation choices from limiting future Haitian Creole research.

Engineering implications: task families, task instances, scientific status, scope status, and release membership require separate machine-readable records. Runtime aliases and currently implemented validators must not be described as the complete project scope.

Risks: roadmap breadth may be mistaken for implementation or commitment; uncontrolled registration may create scope noise without prioritization.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-09 at project-scope governance level. This approval does not validate any v0.1 task specification, taxonomy entry, source, dataset, metric, or release expansion. Independent task-level review remains separately required under `KB-GOV-002`.

Review history:

- 2026-09-09, `APPROVED`, internal project-lead scientific review; evidence: `reports/TASK_SPEC_REVIEW_PACKET_V0_1.md`.

## KB-SRCREV-001

Title: Project-Lead source-feasibility review v0.1

Date: 2026-09-18

Status: EXPERT_VALIDATED

Context: The AI-assisted metadata packet required human review to correct stale evidence, separate scientific feasibility from authorization, and prioritize source-specific next-stage work.

Decision: Accept the metadata methodology with required corrections and adopt the 19 source-specific dispositions recorded in `reports/SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md`. Four sources move from a blocked summary to conditional scientific feasibility; five remain blocked for actionable use; ten retain conditional scientific feasibility. Two sources remain pending Project-Lead review, and later discovery records are outside this review's scope.

Alternatives considered: treat feasibility as authorization; approve every accessible source; leave the original single-label conclusions unchanged; attribute implementation evidence checks to the human reviewer.

Scientific rationale: Multi-axis review preserves scientifically promising resources without erasing unresolved legal, ethical, provenance, contamination, or representativeness constraints.

Engineering implications: Feasibility schema v3 stores independent assessment axes and append-only, explicitly attributed review events. Cross-source prioritization, diversity, and contamination ledgers remain non-authoritative planning artifacts.

Risks: `CONDITIONAL` may still be misread as permission; implementation evidence may be misattributed; broad source families may be mistaken for usable corpora.

Requires expert approval: Yes

Expert decision: Accepted with required corrections by Jeff Pierre on 2026-09-18 as Project Lead and Scientific Reviewer. This decision validates the review methodology and prioritization only. It authorizes no collection, transformation, annotation, derived use, redistribution, scientific inclusion, release membership, or publication claim.

Review history:

- 2026-09-18, `APPROVED`, internal Project-Lead scientific review; evidence: `reports/SOURCE_FEASIBILITY_REVIEW_PACKET_V0_1.md`.

## KB-GOV-002

Title: Independent external task-specification review gate

Date: 2026-09-09

Status: EXPERT_VALIDATED

Context: The project-level governance review was performed by the project lead. Task definitions affect linguistic validity, annotation burden, evaluation interpretation, and publication claims and therefore need review independent of their principal authors.

Decision: No v0.1 task specification may be frozen until at least one qualified reviewer outside the core drafting and implementation team has approved it. Language-sensitive rules require Haitian Creole linguistic expertise. NER and retrieval additionally require task-methodology expertise. Reviewer role, independence, conflicts, date, outcome, and evidence must be recorded.

Alternatives considered: project-lead approval alone; advisory external comments; review only immediately before public release.

Scientific rationale: independent review reduces construct-validity blind spots and makes future publication claims more credible.

Engineering implications: task decisions remain `SUBMITTED_TO_REVIEW`; the decision registry stores append-only review events and evidence paths.

Risks: reviewer availability may delay task freeze; independence can be weakened by undisclosed collaboration or authorship interests.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-09. This is an internal approval establishing an external-review requirement for downstream task decisions.

## KB-GOV-003

Title: Qualified external human review evidence policy

Date: 2026-09-10

Status: EXPERT_VALIDATED

Context: Independent review is not credible or auditable when reviewer identity, institutional context, relevant expertise, conflicts, and dated evidence are absent. AI-assisted or internal reviews can improve drafts but cannot substitute for the external human gate established by `KB-GOV-002`.

Decision: A task can become `EXPERT_VALIDATED` only after its machine-readable review requirements are satisfied by identifiable external human experts. Evidence must record reviewer name, affiliation, expertise tags, independence, conflict status and details where applicable, human attestation, review date, outcome, and a repository evidence path. One reviewer may cover multiple qualifications when documented; several reviewers may collectively cover them. Internal review or automated output without external human ownership cannot count toward an external minimum, and an approval with a disqualifying conflict is invalid.

Alternatives considered: anonymous review; project-lead approval; AI review as external evidence; unstructured email approval without qualification metadata.

Scientific rationale: Qualification and conflict evidence makes construct-level review traceable and reduces the risk of ceremonial approval by reviewers without the required linguistic or methodological competence.

Engineering implications: Decision records carry task-specific `review_requirements`; review events carry affiliation, expertise, and conflict fields; validation checks approval count and collective expertise coverage.

Risks: qualified reviewers may be difficult to recruit; public evidence must avoid unnecessary personal data; affiliations alone do not prove expertise.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-10 as a governance policy. This approval does not validate a task or count as external review.

Review history:

- 2026-09-10, `APPROVED`, internal project-lead scientific review; evidence: `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`.

## KB-TASK-CLS-001

Title: Multi-label topic-classification task specification

Date: 2026-09-09

Status: SUBMITTED_TO_REVIEW

Context: The single-label scaffold conflates topic with source domain and cannot represent documents covering multiple public-interest subjects.

Decision: Propose `kb_cls_topic_multilabel_v0_1`, a multi-label topic instance using a versioned flat scoring ontology and `target.labels`, while keeping source domain, genre, register, source, and audience separate. `other` is mutually exclusive and justified. Agreement requires per-label, set-based, and bootstrapped chance-adjusted analyses. Prediction thresholds are evaluation parameters tuned only on validation data. The ontology and pilot gate remain provisional.

Alternatives considered: single-label topic classification; source-domain prediction; hierarchical labels in v0.1.

Scientific rationale: multi-label targets better represent overlapping topics without turning provenance metadata into prediction labels.

Engineering implications: task configuration, row schema, fixtures, validators, and future metrics require a multi-label contract.

Risks: co-occurring rare labels and ambiguous `other` usage may reduce reliability.

Requires expert approval: Yes

Expert decision: The 2026-09-10 AI-assisted internal audit requested revision. The accepted corrections were implemented and the specification was resubmitted. Qualified external review remains pending under `KB-GOV-003`.

Review history:

- 2026-09-10, `REVISED`, Jeff Pierre, internal project-lead review; evidence: `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`. This event is not external validation.

## KB-TASK-NER-001

Title: Character-span named-entity-recognition task specification

Date: 2026-09-09

Status: SUBMITTED_TO_REVIEW

Context: Canonical BIO labels bind gold annotations to one tokenizer and cannot faithfully represent nested entities.

Decision: Propose `kb_ie_ner_charspan_v0_1` with typed, contiguous spans using zero-based, end-exclusive Unicode code-point offsets over immutable raw text. BIO/BILOU are versioned derived exports. The schema can represent nesting, but routine pilot annotation keeps it disabled until evidence and external approval justify activation. Crossing spans are prohibited; discontinuous cases are flagged and excluded from pilot scoring. The entity ontology remains provisional.

Alternatives considered: canonical flat BIO tags; flat non-overlapping spans.

Scientific rationale: character spans preserve annotation independently of model tokenization and retain nested structures.

Engineering implications: the canonical NER payload becomes raw text plus entity spans; BIO conversion requires versioned tokenization and loss documentation.

Risks: nested annotation increases cognitive load and some baselines cannot consume all gold structures.

Requires expert approval: Yes

Expert decision: The 2026-09-10 AI-assisted internal audit requested revision. The accepted corrections were implemented and the specification was resubmitted. Qualified Haitian Creole linguistic and NER-methodology review remains pending.

Review history:

- 2026-09-10, `REVISED`, Jeff Pierre, internal project-lead review; evidence: `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`. This event is not external validation.

## KB-TASK-RET-001

Title: Hybrid-query information-retrieval task specification

Date: 2026-09-09

Status: SUBMITTED_TO_REVIEW

Context: Inline candidate documents do not represent a reusable retrieval collection and document-derived queries risk lexical leakage.

Decision: Propose `kb_ret_hybrid_query_v0_1` using separate corpus, query, and graded-qrel artifacts. Record one of five governed query origins; exclude document-derived diagnostic queries from the principal test set. Missing qrels remain `UNJUDGED`. Candidate pools combine BM25, character n-gram, multilingual dense, and reranking systems. Evaluation reports judgment coverage, pooling-depth sensitivity, and `bpref` alongside candidate `nDCG@10`. Temporal snapshots and query-family grouping are mandatory.

Alternatives considered: expert-authored queries only; document-derived queries only; inline candidates per row.

Scientific rationale: a hybrid design balances ecological validity, controllability, and reproducible evaluation.

Engineering implications: retrieval validation and evaluation operate on linked artifact files rather than canonical `KreyolBenchRow` examples.

Risks: obtaining real information needs may require consent; pooling can leave relevant documents unjudged.

Requires expert approval: Yes

Expert decision: The 2026-09-10 AI-assisted internal audit requested revision. The accepted corrections were implemented and the specification was resubmitted. Qualified Haitian public-information and information-retrieval review remains pending.

Review history:

- 2026-09-10, `REVISED`, Jeff Pierre, internal project-lead review; evidence: `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`. This event is not external validation.

## KB-TASK-NORM-001

Title: Orthography-only text-normalization task specification

Date: 2026-09-09

Status: SUBMITTED_TO_REVIEW

Context: The current example performs lexical expansion, which confounds orthographic normalization with rewriting.

Decision: Propose `kb_norm_orthography_v0_1` with spelling convention, spacing, apostrophe, and diacritic changes as the core construct. Capitalization and punctuation are separately tagged auxiliary strata excluded from the primary score pending external review. Unicode and typographic cleanup are deterministic preprocessing. Gold decisions distinguish error correction, acceptable-variant normalization, accept-as-is, and abstention; every linguistic edit requires versioned normative evidence. Multiple acceptable references remain permitted.

Alternatives considered: broad standardization; grammatical correction; a single canonical target.

Scientific rationale: a narrow construct supports interpretable evaluation while preserving legitimate Haitian Creole variation.

Engineering implications: normalization targets become reference lists with typed edit records and explicit raw-text linkage.

Risks: the boundary between spelling variation and lexical variation requires linguistic adjudication.

Requires expert approval: Yes

Expert decision: The 2026-09-10 AI-assisted internal audit requested revision. The accepted corrections were implemented and the specification was resubmitted. Qualified Haitian Creole orthography review remains pending.

Review history:

- 2026-09-10, `REVISED`, Jeff Pierre, internal project-lead review; evidence: `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`. This event is not external validation.

## KB-TASK-CS-001

Title: Token-level code-switching task specification

Date: 2026-09-09

Status: SUBMITTED_TO_REVIEW

Context: BIO language tags redundantly encode sequence boundaries and conflate language identity with token type.

Decision: Propose `kb_lc_token_language_id_v0_1` with versioned token offsets and a factorized annotation containing `language_id`, `token_type`, `contact_status`, and uncertainty. Established Haitian Creole borrowings use `hat` plus `ESTABLISHED_BORROWING`; etymology and named-entity origin never determine language identity automatically. `mul` is reserved for inseparable mixed forms and `und` for genuine contextual uncertainty. Derived active-switch boundaries exclude punctuation, borrowing, `und`, and `zxx`.

Alternatives considered: BIO language tags; sentence labels only; language and token type in one label vocabulary.

Scientific rationale: direct language identification is simpler, more extensible, and analytically separable from punctuation, numbers, names, and other token types.

Engineering implications: sentence labels are removed from canonical targets; derived composition is computed from token labels.

Risks: borrowings, cognates, named entities, clitics, and intra-token mixing may have low agreement.

Requires expert approval: Yes

Expert decision: The 2026-09-10 AI-assisted internal audit requested revision. The accepted corrections were implemented and the specification was resubmitted. Qualified Haitian Creole sociolinguistic and language-contact review remains pending.

Review history:

- 2026-09-10, `REVISED`, Jeff Pierre, internal project-lead review; evidence: `reports/INTERNAL_TASK_SCIENTIFIC_AUDIT_V0_1.md`. This event is not external validation.

## KB-ENG-001

Title: Machine-readable governance registry

Date: 2026-09-08

Status: TO_REVIEW_LATER

Context: Markdown decision records are authoritative research memory but are not a reliable runtime validation interface.

Decision: Maintain executable decision identifiers and statuses in `configs/governance/decisions.yaml`. Require each machine-readable record to have a matching narrative record in this file with the same status.

Alternatives considered: Parse all Markdown semantics at runtime; keep status only in prose; duplicate the full rationale in YAML.

Scientific rationale: None; this is an engineering traceability mechanism and does not validate scientific content.

Engineering implications: Configuration audits fail on missing decision references or status drift between the YAML registry and this document.

Risks: Duplicate representations can drift if updates bypass the governance audit.

Requires expert approval: No

Expert decision: Not required

## KB-ENG-002

Title: Structural validity and release eligibility separation

Date: 2026-09-08

Status: TO_REVIEW_LATER

Context: KreyolBench must support ongoing engineering while scientific decisions remain unresolved.

Decision: A governance audit may return `PASS` when files and invariants are structurally valid while reporting `release_eligible: false` because scientific approvals remain pending. Structural errors return `FAIL` and a nonzero CLI exit code.

Alternatives considered: Fail every audit while any scientific decision is pending; treat a structurally valid repository as release-ready.

Scientific rationale: The distinction prevents provisional implementation from being misrepresented as scientific validation.

Engineering implications: CI can enforce structural correctness without bypassing expert review gates.

Risks: Users may read `PASS` without checking release eligibility; CLI output therefore reports both fields prominently.

Requires expert approval: No

Expert decision: Not required

## KB-ENG-003

Title: Multi-axis source-registry schema version 2

Date: 2026-09-09

Status: TO_REVIEW_LATER

Context: The legacy source `review_status` mixed discovery, legal review, permissions, ethics, and scientific inclusion into one value.

Decision: Replace committed source records with schema version 2 and typed, independent governance axes. Keep a temporary read compatibility layer for legacy `SourcePlan` consumers, while the repository audit rejects committed schema-v1 configs.

Alternatives considered: add more values to the legacy enum; use unvalidated free-text statuses; postpone enforcement.

Scientific rationale: None beyond faithfully implementing the validated separation of scientific and authorization decisions.

Engineering implications: source configs, adapters, audits, and tests use the v2 model. Deprecated compatibility properties summarize v2 states but are not authoritative.

Risks: external callers may rely on legacy status strings; redundant compatibility views may be misused.

Requires expert approval: No

Expert decision: Not required

## KB-ENG-004

Title: Example-level provenance and content-origin contract

Date: 2026-09-09

Status: TO_REVIEW_LATER

Context: Source-registry records govern candidate collections, but `KB-DATA-001` also requires every example to retain granular provenance and distinguish original, translated, generated, transcribed, and OCR-derived content.

Decision: Add a typed example provenance model with a specific source unit, stable item locator, version, retrieval date, content hash, origin type, and ordered derivation steps. A `SOURCE_FAMILY` may never serve as final example provenance.

Alternatives considered: source ID only; free-text origin notes; machine-generation risk only.

Scientific rationale: This engineering contract implements already validated provenance requirements without granting source authorization or scientific inclusion.

Engineering implications: committed sample fixtures use synthetic origin metadata; validators enforce specific-source linkage and derivation-step structure.

Risks: locators may expose sensitive identifiers unless release views redact them; incomplete transformation chains may create false confidence.

Requires expert approval: No

Expert decision: Not required

## KB-ENG-005

Title: Extensible task taxonomy and release-membership registry

Date: 2026-09-09

Status: TO_REVIEW_LATER

Context: Existing task slugs, `v0` booleans, and one benchmark-level task list conflated runtime implementation, scientific scope, and release membership.

Decision: Use stable task-instance identifiers linked to open-world task families and task types. Store scientific review status separately from scope status, and make versioned release records authoritative for release membership. Preserve current task slugs as compatibility aliases rather than treating them as the global task universe.

Alternatives considered: retain the fixed `v0_tasks` list; place all future task names in a Python enum; duplicate release booleans across benchmark and task files.

Scientific rationale: None beyond faithfully representing bounded releases within the proposed open-world research program.

Engineering implications: governance audits resolve family, type, instance, and release references and reject invalid inclusion states.

Risks: compatibility aliases may be mistaken for stable scientific identifiers; registries can drift if audits are bypassed.

Requires expert approval: No

Expert decision: Not required

## KB-ENG-006

Title: Machine-enforced reviewer qualification and evidence checks

Date: 2026-09-10

Status: TO_REVIEW_LATER

Context: `KB-GOV-003` requires auditable external-review qualifications and conflicts rather than relying on a status label alone.

Decision: Extend review events with affiliation, expertise tags, conflict status, conflict details, and human attestation. Extend decisions with explicit external-review requirements. Validate minimum qualifying approval count, collective expertise coverage, evidence-file existence, and latest-event/status consistency.

Alternatives considered: prose-only checks; one universal reviewer role; accepting internal approvals for externally gated tasks.

Scientific rationale: None beyond enforcing the validated governance policy faithfully.

Engineering implications: governance schema version 4 rejects incomplete external reviews, disqualifying conflicts, and task validation based only on internal events.

Risks: machine-readable tags can overstate competence unless evidence is reviewed; public records must minimize personal data.

Requires expert approval: No

Expert decision: Not required

## KB-ENG-007

Title: Machine-readable metadata-only source-feasibility ledger

Date: 2026-09-10

Status: TO_REVIEW_LATER

Context: Source-registry authorization axes do not express the strength of public metadata evidence available for deciding which candidates deserve legal, ethical, linguistic, or scientific follow-up.

Decision: Maintain one versioned feasibility record for every registered research candidate and a separate synthetic-control record. Each record reports eight evidence dimensions, authoritative URLs, unresolved claims, candidate task fit, and permitted next-review actions. Its authorization effect is always `NONE`.

Alternatives considered: encode feasibility in free-text source notes; treat endpoint visibility as permission; add numeric readiness scores; review only pilot-facing sources.

Scientific rationale: None beyond preserving a reviewable boundary between factual metadata evidence and later human authorization or scientific-inclusion decisions.

Engineering implications: `audit-governance` enforces complete registry coverage, evidence paths, task references, non-authorizing conclusions, and unchanged source gates.

Risks: evidence may become stale; official pages can be incomplete; a `CONDITIONAL` conclusion may be misread as approval unless the no-authorization rule remains prominent.

Requires expert approval: No

Expert decision: Not required

## KB-ENG-008

Title: Open-world discovery intake and claim-level metadata evidence

Date: 2026-09-10

Status: TO_REVIEW_LATER

Context: Repeated resource names, derivatives and unverified language claims must not inflate corpus coverage or imply authorization.

Decision: Preserve each intake, deduplicate canonical resource/configuration/revision identities, separate registered sources from unresolved leads and references, and record evidence-backed relationships without inheriting rights. Feasibility schema v2 requires direct claim evidence for every EVIDENCE_AVAILABLE dimension. Historical schema-v1 evidence remains archived.

Alternatives considered: append every mention as a dataset; force references into source configs; retain one generic evidence URL for all dimensions.

Scientific rationale: No new task, metric, release membership, source permission or scientific approval is introduced.

Engineering implications: Discovery is a separate typed module integrated into the existing audit. Coverage is registry-driven rather than fixed at 21. Reported sizes retain units, revisions and evidence; they are never automatically summed.

Risks: metadata can be stale or wrong; machine validation checks evidence structure, not truth. Broad domain mappings are hypotheses, not coverage measurements.

Requires expert approval: No

Expert decision: Not required for engineering; source findings remain SUBMITTED_TO_REVIEW or BLOCKED.

## KB-ENG-009

Title: Append-only multi-axis source-review evidence and attribution

Date: 2026-09-18

Status: TO_REVIEW_LATER

Context: A single feasibility label could erase independent scientific and authorization axes, while untyped prose could blur human decisions with Codex evidence checks.

Decision: Use feasibility schema v3 with independent assessment axes, append-only source-review events, structured external-evidence requirements, and complete planning ledgers for prioritization, representativeness, and contamination. Human decisions and implementation evidence checks use distinct event types and attribution rules.

Alternatives considered: overwrite the earlier assessment; store only an overall conclusion; infer human approval from updated evidence; duplicate authorization states as informal prose.

Scientific rationale: None beyond faithfully preserving the Project-Lead review and the validated multi-axis source-governance policy.

Engineering implications: Audits reject incomplete inventory coverage, false human attribution, unsupported contamination-free claims, and any feasibility record paired with an authorized source state.

Risks: More structured metadata increases maintenance cost; categorical planning evidence can become stale; a structurally valid record does not establish factual truth.

Requires expert approval: No

Expert decision: Not required

## KB-SRCREV-002

Title: Project-Lead expanded source-discovery review

Date: 2026-09-18

Status: EXPERT_VALIDATED

Context: Twenty-one supplied resources or references required explicit dispositions without converting metadata discovery into source authorization.

Decision: Accept the source-specific metadata dispositions and required corrections recorded in `reports/SOURCE_DISCOVERY_EXPANSION_REVIEW_PACKET_V0_1.md`. The discovery packet is validated only for metadata identity, scientific-role triage, prioritization, and reconciliation. No acquisition, training, annotation, redistribution, scientific inclusion, task approval, or release authorization follows.

Alternatives considered: treating every public endpoint as usable data; collapsing mirrors and upstream sources; crediting methodology references as Haitian corpus coverage; leaving training and evaluation roles implicit.

Scientific rationale: Broad discovery protects KreyolBench's open-world ambition, while resource-specific provenance and use firewalls protect validity, rights, community trust, and future benchmark independence.

Engineering implications: The discovery, source-use, feasibility, contamination, and diversity ledgers must preserve exact identities, lineage, attribution, unresolved evidence, and authorization effect `NONE`.

Risks: Scientific priority can be misread as permission; reported sizes can be mistaken for unique examples; translated or web-derived resources can obscure origin and contamination.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre, Project Lead and Scientific Reviewer, on 2026-09-18 after human review of the evidence and an AI-assisted research synthesis. Independence: `INTERNAL_PROJECT_LEAD`.

## KB-DATA-004

Title: Source roles, use eligibility, and contamination firewall

Date: 2026-09-18

Status: EXPERT_VALIDATED

Context: A source can be scientifically interesting while remaining prohibited for training, unsuitable for gold evaluation, legally unresolved, ethically restricted, or excluded from release.

Decision: Maintain scientific roles, training eligibility, evaluation eligibility, contamination status, legal status, ethics status, scientific inclusion, and release membership as independent axes. Protected evaluation material cannot enter training pools. Mirrors and aggregators cannot transfer rights or provenance automatically.

Alternatives considered: one approved/blocked label; deriving eligibility from a license badge; allowing benchmark components into training when overlap is unknown.

Scientific rationale: The firewall prevents circular evaluation, hidden contamination, and invalid claims while preserving useful comparison and methodology references.

Engineering implications: Every registered source and unresolved/reference lead receives a source-use and contamination record. Frozen release inputs require immutable revisions, hashes, split identity, and ordered derivation provenance.

Risks: Eligibility may become stale as evidence changes; component-level overlap can remain unknown; conservative prohibitions may reduce short-term data volume.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-18 at project-policy level. It grants no source-specific authorization.

## KB-DATA-005

Title: Native-versus-translated multimodal provenance policy

Date: 2026-09-18

Status: EXPERT_VALIDATED

Context: A multilingual image-caption resource can contain Haitian translations without being a native Haitian Creole vision-language dataset, and media rights can differ from caption rights.

Decision: Track media provenance, caption authoring origin, translation route, transformations, linkage, rights, split identity, parent datasets, and contamination independently. Do not credit a resource as native Haitian Creole multimodal coverage without direct evidence.

Alternatives considered: infer native coverage from a language code; collapse media and caption rights; classify machine-translated captions as human-original Haitian data.

Scientific rationale: Native cultural grounding, translated evaluation, and methodology transfer answer different research questions and must remain distinguishable.

Engineering implications: Typed multimodal provenance uses canonical content-origin categories and ordered derivation steps. The current absence of a validated native Haitian Creole vision-language source remains an explicit evidence gap.

Risks: Provider documentation may omit authoring origin or image rights; machine-translation pipelines may be incompletely reported.

Requires expert approval: Yes

Expert decision: Approved by Jeff Pierre on 2026-09-18 at project-policy level. It validates provenance requirements, not XM3600 or VICR as Haitian datasets.

## KB-ENG-010

Title: Machine-enforced source-use, contamination-firewall, and multimodal-provenance schemas

Date: 2026-09-19

Status: TO_REVIEW_LATER

Context: The validated source policies require deterministic enforcement across registered sources and unresolved discovery leads.

Decision: Add complete source-use and contamination ledgers, canonical content-origin values, ordered derivation provenance, independent media and caption provenance, protected-split training prohibitions, and exact coverage audits.

Alternatives considered: prose-only policy; task-specific hard coding; relying on source cards without repository validation.

Scientific rationale: None beyond faithfully enforcing `KB-DATA-004` and `KB-DATA-005`.

Engineering implications: Structural audit can pass while release eligibility remains false. Machine validation checks internal consistency, not legal truth or scientific quality.

Risks: Strict schemas increase maintenance cost and cannot replace qualified human review.

Requires expert approval: No

Expert decision: Not required

## Revision History

| Date | Change | Status |
| --- | --- | --- |
| 2026-09-01 | Initial decision register and first seven decision records. | IN_PROGRESS |
| 2026-09-08 | Added executable-governance and audit-semantics engineering decisions. | IN_PROGRESS |
| 2026-09-09 | Reconciled expert decisions, added open-world discovery and v0.1 scope decisions, and documented source schema v2. | IN_PROGRESS |
| 2026-09-09 | Closed KB-DATA-001, added independent task review, five provisional task decisions, and example-level provenance traceability. | IN_PROGRESS |
| 2026-09-09 | Added the open-world task-scope proposal and extensible taxonomy/release architecture. | IN_PROGRESS |
| 2026-09-10 | Recorded the internal task audit, qualified external-review policy, five revision events, and reviewer-evidence enforcement. | IN_PROGRESS |
| 2026-09-10 | Added the metadata-only source-feasibility ledger decision without changing source authorization. | IN_PROGRESS |
| 2026-09-18 | Recorded the Project-Lead source-feasibility review and append-only multi-axis evidence architecture. | IN_PROGRESS |
| 2026-09-19 | Implemented the expanded Project-Lead source decisions, source-use firewall, contamination lineage, and multimodal provenance policy. | IN_PROGRESS |
