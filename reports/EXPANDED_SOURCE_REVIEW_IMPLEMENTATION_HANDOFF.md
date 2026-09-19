# Expanded Human Source-Review Implementation Handoff

## Status

Current status: `EXPERT_VALIDATED` for implementation of metadata-discovery decisions and project-level source-governance policies only.

Release eligible: `false`.

Authorization effect: `NONE`.

## Human Decisions Implemented

The source decisions were made by the Project Lead, Jeff Pierre, after human review of the evidence and an AI-assisted research synthesis. Reviewer role: Project Lead and Scientific Reviewer. Date: 2026-09-18. Independence: `INTERNAL_PROJECT_LEAD`.

Implemented decisions: `KB-SRCREV-002`, `KB-DATA-004`, and `KB-DATA-005`. `KB-ENG-010` records the engineering implementation as `TO_REVIEW_LATER`.

This work does not constitute independent external review, legal advice, ethics-board review, task validation, or source authorization.

## Files Modified

- Governance: `DECISIONS.md`, `configs/governance/decisions.yaml`, discovery, feasibility, prioritization, diversity, and contamination ledgers.
- Source records: FLORES+, xP3x, FinePDFs, mC4, CreoleVal, MIT-Haiti via CreoleVal, CMU family/mirror, Babel, Kreyol-MT, Wikimedia snapshot, both UD treebanks, and Mission 4636 family.
- Code: source-assessment, source-discovery, provenance-schema, and source-family validation modules.
- Research memory: roadmap, changelog, source-to-task matrix, discovery packet, dataset/report indexes, and 21 reviewed source reports.
- Fixtures and tests: canonical synthetic origin values and source-governance regression coverage.

## Files Created

- `configs/governance/source_use.yaml`
- `configs/sources/voxlingua107_hat.yaml`
- `configs/sources/northern_haitian_creole_corpus.yaml`
- `configs/sources/mission_4636_open_nonsensitive.yaml`
- `configs/sources/mission_4636_restricted_sensitive.yaml`
- `datasets/SOURCE_USE_POLICY.md`
- `datasets/MULTIMODAL_PROVENANCE.md`
- `reports/CREOLEVAL_HAITIAN_COMPONENT_MATRIX_V0_1.md`
- Four matching source-review reports for the newly registered records
- `tests/test_expanded_source_review.py`
- This handoff report

## Source-by-Source Final State

All scientific roles are provisional. `REQUIRES_REVIEW` is not authorization.

| Resource | Discovery and identity | Scientific role | Rights and ethics | Acquisition / redistribution / inclusion | Training / evaluation / contamination | Remaining blocker |
| --- | --- | --- | --- | --- | --- | --- |
| FLORES+ `hat_Latn` | Registered; release 4.6 metadata; immutable hashes pending | Protected evaluation and contamination reference | Provider license documented; attribution and release interpretation unresolved | Not authorized / unresolved / not included | Prohibited / protected reference / elevated | Pin files and hashes; reconcile overlap and redistribution obligations. |
| xP3x Haitian | Registered instruction mixture; upstream lineage partial | Instruction tuning and contamination reference | Aggregate license documented; component rights and origin vary | Not authorized / unresolved / not included | Review required / primary evaluation prohibited / elevated | Component lineage, prompt duplication, and FLORES overlap. |
| jsbeaudry continued-pretraining | Unverified lead; approximately 11.1k rows, not verified unique documents | Pretraining candidate only | Rights, authorship, generation, and representativeness unknown | Not authorized / unresolved / not included | Review required / prohibited / elevated | Provider, provenance, STEM composition, rights, and uniqueness. |
| Haitian Wikipedia snapshot | Registered snapshot child; page/revision provenance required | Corpus, pretraining, retrieval, NER/classification discovery | Wikimedia text terms documented with content/media exceptions; biography risks remain | Not authorized / conditional evidence / not included | Review required / contamination review required / elevated | Immutable extraction, attribution, page-level exceptions, dominance control, and contamination. |
| FinePDFs Haitian | Registered web/PDF/OCR collection | Pretraining, OCR, and discovery | ODC-By distribution plus Common Crawl/source dependencies; residual PII/OCR risks | Not authorized / unresolved / not included | Review required / gold evaluation prohibited / elevated | Haitian validation, original-document rights, PII, OCR quality, deduplication, and origin. |
| mC4 Haitian | Registered automatically language-identified web collection | Pretraining and robustness | Distribution and Common Crawl dependencies documented; content rights/PII unresolved | Not authorized / unresolved / not included | Review required / gold evaluation prohibited / elevated | Language revalidation, URL provenance, content risk, domain inventory, deduplication. |
| JHU Kreyol-MT | Registered aggregate family; pair/upstream children required | Future MT and contamination reference | Aggregate `other` terms; component rights and translation origins unresolved | Not authorized / unresolved / excluded from v0.1 | Review required / review required / elevated | Pair-level child records, licenses, origins, hashes, and overlaps. |
| CreoleVal | Registered benchmark family | Mandatory comparison and contamination reference | Heterogeneous component terms | Not authorized / unresolved / not included as one corpus | Prohibited / protected comparison reference / elevated | Complete Haitian component/license/overlap matrix before novelty or use claims. |
| MIT-Haiti via CreoleVal | Registered subset candidate; asset classes separated | Educational/parallel gold-data candidate | Exact license instrument and asset identity unresolved | Not authorized / unresolved / not included | Review required / review required / known parent overlap | Verify exact parallel subset, license, hashes, and relation to other MIT-Ayiti assets. |
| CMU original family | Registered non-content-bearing family | High-value speech/corpus family | Original component rights, consent, and current artifacts unresolved | Not authorized / unresolved / not included | Review required / review required / not established | Separate speech, transcripts, ASR/TTS, lexicon, text, and medical-phrase children. |
| phatjmo CMU mirror | Registered mirror child | Mirror and identity/hash reference | Mirror badge does not transfer original CMU rights | Not authorized / prohibited as rights shortcut / not included | Prohibited / prohibited / known parent relation | Reconcile hashes and transport identity against original CMU artifacts and terms. |
| Babel LDC2017S03 | Registered restricted collection; regional/telephone metadata documented | Restricted high-value speech resource | LDC agreements required; minors, consent, privacy, and ethics need review | Restricted, not acquired / prohibited / not included | Review required under agreement / review required / not established | Agreement, ethics/privacy review, demographics, and speaker-disjoint design. |
| VoxLingua107 Haitian | Registered metadata source; provider reports about 96 hours; no transcript claim | Speech language-ID/acoustic candidate | Source-video rights, consent, deletion, and redistribution unresolved | Not authorized / unresolved / not included | Review required / review required / not established | Immutable release, source lineage, rights, consent, and demographic bias. |
| Northern Haitian corpus | Scholarly documented and registered; archive unavailable | Regional speech and linguistic priority | Custodian, consent, license, exact release, and ethics unresolved | Blocked / unresolved / not included | Prohibited while blocked / review unavailable / not assessed | Recover authoritative archive and verify speakers, transcripts, consent, version, and rights. |
| UD Autogramm | Registered UD child pinned to 2.18 | High-priority morphosyntax, robustness, and regional reference | CC BY-SA treebank metadata; upstream-text rights remain separate | Not authorized / conditional evidence / not included | Review required / review required / elevated | Upstream text rights, hashes, source balance, conversion quality, and representativeness limits. |
| UD Adolphe | Registered UD child pinned to 2.18 | Limited religious-domain linguistic reference | CC BY-SA treebank metadata; upstream Bible rights separate | Not authorized / conditional evidence / not included | Review required / review required / elevated | Upstream text rights, conversion provenance, hashes, and strict domain limitation. |
| Mission 4636 family | Registered non-content-bearing family with two governed children | Humanitarian-language and disaster-response discovery family | Public-interest origin is not consent | Family cannot be acquired or redistributed / not included | Not a training/evaluation artifact / contamination reference | Select an exact artifact through custodian and ethics review. |
| Mission 4636 open/non-sensitive child | Conceptual registered child; exact artifact unresolved | Gold/corpus candidate for retrieval, language contact, robustness | Privacy-selection and residual sensitivity require evidence | Not authorized / conditional unresolved / not included | Review required / review required / known family overlap | Custodian, exact artifact, terms, privacy selection, PII, translation history, hashes. |
| Mission 4636 restricted/sensitive child | Registered restricted metadata child | Restricted research reference | Formal custodian and ethics authorization required | Prohibited / prohibited / not included | Prohibited / prohibited / known family overlap | No ordinary-pipeline action; formal ethics and custodian decision only. |
| APiCS structure 49 | Reference-only, versioned scholarly identity | Linguistic/typological methodology | APiCS terms and citation apply | No corpus acquisition / no benchmark redistribution / not included | Not applicable / reference only / not assessed | Version/citation preservation and separate validation for any derived challenge set. |
| APiCS survey 49 | Reference-only scholarly identity | Sociolinguistic context | APiCS terms and citation apply | No general corpus acquisition / not included | Not applicable / reference only / not assessed | Do not project historical claims onto the current population without new evidence. |
| XM3600 | Verified methodology reference; Haitian coverage not established | Multimodal methodology and contamination reference | Image and caption rights remain independent | No Haitian acquisition / none / no Haitian inclusion | Not applicable / reference only / elevated reference | Optional authoritative language-inventory check; no Haitian coverage credit. |
| Translated VICR lead | Methodology paper verified; Haitian release unverified and blocked | Multimodal and machine-translated-evaluation methodology reference | Underlying image and caption rights unresolved | No Haitian acquisition / none / no Haitian inclusion | Not applicable / reference only / elevated reference | Authoritative Haitian release, provenance, quality, cultural validity, rights, and human revalidation. |

## Claims Corrected

- Replaced “11.1k documents” with approximately 11.1k reported rows; uniqueness and STEM representativeness remain unverified.
- Removed claims that Aya contains millions of human-written Haitian conversations; parent material includes templated and machine-translated resources.
- Reclassified xP3x as an instruction-training mixture, not independent evaluation gold.
- Tied Wikipedia counts to an exact snapshot and rejected automatic factual-quality or native-authorship claims.
- Separated UD Autogramm from Adolphe and pinned version-specific metadata.
- Rejected the CMU mirror's badge as proof of original rights.
- Documented Babel as restricted, not open, and flagged the reported age range's inclusion of minors.
- Verified VoxLingua Haitian metadata without inventing transcripts or ASR-gold status.
- Upgraded Northern Haitian identity from a mere claim while keeping acquisition blocked.
- Split Mission 4636 open/non-sensitive and restricted/sensitive governance.
- Kept XM3600 and translated VICR from counting as Haitian multimodal data.
- Replaced legacy origin labels with canonical, non-quality content-origin categories.

## New Evidence Recorded

- Provider-level FLORES+, xP3x, FinePDFs, mC4, VoxLingua107, Babel, CreoleVal, XM3600, APiCS, and Wikimedia metadata.
- Version-specific UD 2.18 treebank statistics and provenance limitations.
- Mission 4636 child-level privacy and access distinctions.
- CreoleVal component-level license and overlap requirements.
- A native Haitian Creole vision-language `EVIDENCE_GAP` rather than invented coverage.

## Contamination Controls

- Every registered non-synthetic source and every unresolved/reference lead has one contamination record.
- FLORES+ dev/devtest and CreoleVal evaluation components are protected and training-prohibited.
- Parent, child, mirror, snapshot, and known-overlap relationships are explicit.
- `CONTAMINATION_NOT_ESTABLISHED` is distinct from contamination-free; `CONTAMINATION_FREE` is prohibited by validation.
- Frozen use requires exact subset, split, revision, hashes, and ordered provenance.

## Provenance Controls

- Canonical origins distinguish human-original, human-translated, machine-translated, LLM-generated, synthetic, ASR-derived, OCR-derived, human-transcribed, mixed, and unknown material.
- Ordered derivation steps preserve transformations without erasing deeper origin.
- Families cannot back example-level provenance.
- Multimodal media, captions, authoring/translation origin, rights, linkage, split, and contamination are independently represented.

## Unresolved External Questions

- Rights-holder or legal review: exact asset permissions, redistribution, commercial use, and upstream component terms.
- Ethics review: speech consent, minors, crisis-message sensitivity, PII, dignity, retention, and deletion.
- Haitian Creole expert review: language quality, orthography, regional/register claims, and cultural validity.
- Archive/provider clarification: CMU components, Northern Haitian access, Mission 4636 artifacts, and immutable releases.
- Contamination review: benchmark overlap, instruction-mixture lineage, public web/religious reuse, and protected split integrity.

## Test Results

- Ruff: `PASS`.
- Full test suite, including the immutable-release invariant: `182 passed` in 154.66 seconds, executed by the Project Lead on 2026-09-19.
- Targeted source/provenance suite: `66 passed`.
- The earlier Codex-hosted rerun was environment-blocked after macOS reported `No space left on device`; the subsequent Project-Lead execution confirms the complete suite passes.

## Governance Audit

- Last completed audit before the final immutable-release invariant: `PASS`.
- Errors: `0`.
- Warnings: `0`.
- Unresolved decisions: exactly `KB-TASK-CLS-001`, `KB-TASK-CS-001`, `KB-TASK-NER-001`, `KB-TASK-NORM-001`, and `KB-TASK-RET-001`.

## Release Eligibility

`false`

No source authorization axis, task decision, or v0.1 release membership was elevated.

The CLI governance audit still requires execution from a Python environment containing the declared project dependencies. A shell-level `python3.12` without `typer` is not a valid project runtime.

## Next Human Review Gate

Select a small bounded set of high-priority child resources, beginning with exact AKA normative documents, a Wikimedia snapshot extraction specification, the MIT-Haiti parallel subset, VoxLingua107 metadata clarification, and the Mission 4636 open/non-sensitive artifact question. For each, obtain the appropriate rights-holder/legal, ethics, Haitian Creole linguistic, and contamination review before any acquisition request. Continue independent external review of the five task specifications in parallel.

Stop before acquisition, annotation, training, final split construction, task validation, or release preparation.
