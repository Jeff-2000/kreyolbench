# Source Domain and Modality Discovery Matrix

Current status: SUBMITTED_TO_REVIEW

Prepared by: Codex, AI-assisted. Date: 2026-09-10. Authorization effect: NONE.

Historical role: this discovery matrix records the 2026-09-10 expansion view. The active representativeness projection is `configs/governance/source_diversity.yaml`, documented in `datasets/SOURCE_DIVERSITY.md`. Neither artifact measures achieved corpus coverage or authorizes source use.

## Interpretation

This matrix combines original registry domain claims with the new intake's candidate domain mappings. A candidate is not measured coverage. Absence means a discovery gap in this inventory, not evidence that no resource exists. Reference-only and unverified leads cannot satisfy corpus coverage.

| Domain | Existing metadata candidates | Expansion leads (including references) | Required follow-up |
| --- | --- | --- | --- |
| health | None explicitly mapped | `cmu_original` | Verify language, subdomain, register, rights and representativeness |
| education | `mit_ayiti_resources`, `menfp_educational_resources` | `wikipedia_20231101_ht`, `mit_haiti_parallel` | Verify language, subdomain, register, rights and representativeness |
| civic_admin | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| disaster_response | `haiti_civil_protection_resources` | `munro_sms` | Verify language, subdomain, register, rights and representativeness |
| religion | `ebible_hat_1985` | `ud_autogramm`, `ud_adolphe` | Verify language, subdomain, register, rights and representativeness |
| news | `haitian_news_candidates` | `ud_autogramm` | Verify language, subdomain, register, rights and representativeness |
| culture | None explicitly mapped | `apics_survey49` | Verify language, subdomain, register, rights and representativeness |
| other | None explicitly mapped | `flores_plus_hat`, `xp3x_hat`, `aya_haitian`, `finepdfs_hat`, `mc4_ht`, `kreyol_mt`, `creoleval`, `cmu_hf_mirror`, `voxlingua107_hat`, `apics_structure49`, `xm3600`, `vicr_translated` | Verify language, subdomain, register, rights and representativeness |
| agriculture | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| environment | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| justice_law | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| economics | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| finance | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| migration | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| diaspora | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| science_stem | None explicitly mapped | `jsbeaudry_stem`, `mit_haiti_parallel` | Verify language, subdomain, register, rights and representativeness |
| history | None explicitly mapped | `apics_survey49` | Verify language, subdomain, register, rights and representativeness |
| literature | None explicitly mapped | `ud_autogramm` | Verify language, subdomain, register, rights and representativeness |
| social_media | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| everyday_conversation | None explicitly mapped | `babel_haitian`, `northern_haitian` | Verify language, subdomain, register, rights and representativeness |
| labor_employment | None explicitly mapped | None explicitly mapped | Discovery gap; seek named collections without inferring availability |
| humanitarian_response | None explicitly mapped | `munro_sms` | Verify language, subdomain, register, rights and representativeness |

## Modality and Research Pathways

| Lead | Modalities | Candidate task families | Current task instances | Boundary |
| --- | --- | --- | --- | --- |
| jsbeaudry_stem | text | llm_evaluation | None asserted | UNVERIFIED_LEAD; unvalidated fit |
| wikipedia_20231101_ht | text | classification, information_extraction, retrieval | kb_cls_topic_multilabel_v0_1, kb_ie_ner_charspan_v0_1, kb_ret_hybrid_query_v0_1 | REGISTERED_SOURCE; unvalidated fit |
| flores_plus_hat | text | translation | None asserted | REGISTERED_SOURCE; unvalidated fit |
| xp3x_hat | text | llm_evaluation | None asserted | REGISTERED_SOURCE; unvalidated fit |
| aya_haitian | text | llm_evaluation | None asserted | REGISTERED_SOURCE; unvalidated fit |
| finepdfs_hat | text, document | classification, retrieval, document_multimodal | kb_cls_topic_multilabel_v0_1, kb_ret_hybrid_query_v0_1 | REGISTERED_SOURCE; unvalidated fit |
| mc4_ht | text | linguistic_robustness, normalization, language_contact | kb_norm_orthography_v0_1, kb_lc_token_language_id_v0_1 | REGISTERED_SOURCE; unvalidated fit |
| kreyol_mt | text | translation | None asserted | REGISTERED_SOURCE; unvalidated fit |
| creoleval | text | linguistic_robustness | None asserted | REGISTERED_SOURCE; unvalidated fit |
| mit_haiti_parallel | text | translation | None asserted | REGISTERED_SOURCE; unvalidated fit |
| cmu_original | speech, text | speech_audio | None asserted | REGISTERED_SOURCE; unvalidated fit |
| cmu_hf_mirror | speech, text | speech_audio | None asserted | REGISTERED_SOURCE; unvalidated fit |
| babel_haitian | speech, text | speech_audio | None asserted | REGISTERED_SOURCE; unvalidated fit |
| voxlingua107_hat | speech | speech_audio, language_contact | None asserted | UNVERIFIED_LEAD; unvalidated fit |
| northern_haitian | speech, text | speech_audio, linguistic_robustness | None asserted | UNVERIFIED_LEAD; unvalidated fit |
| ud_autogramm | text | linguistic_robustness | None asserted | REGISTERED_SOURCE; unvalidated fit |
| ud_adolphe | text | linguistic_robustness | None asserted | REGISTERED_SOURCE; unvalidated fit |
| munro_sms | text | language_contact, retrieval | kb_ret_hybrid_query_v0_1, kb_lc_token_language_id_v0_1 | REGISTERED_SOURCE; unvalidated fit |
| apics_survey49 | text | linguistic_robustness, language_contact | None asserted | REFERENCE_ONLY; unvalidated fit |
| apics_structure49 | structured_linguistic | linguistic_robustness | None asserted | REFERENCE_ONLY; unvalidated fit |
| xm3600 | image, text | document_multimodal | None asserted | REFERENCE_ONLY; unvalidated fit |
| vicr_translated | image, text | document_multimodal | None asserted | UNVERIFIED_LEAD; unvalidated fit |

Speech, multilingual translation, instruction tuning, syntax and multimodal references remain ecosystem pathways. No runtime adapters, annotation protocols or release memberships are created. NER and normalization are not automatically derivable gold tasks from a treebank or pretraining collection.

## Next Action

Select a few clearly bounded, ethically reviewable collections for human feasibility review. Retain open gaps in law, agriculture, finance, migration and other domains rather than manufacturing completeness through broad web-resource labels.
