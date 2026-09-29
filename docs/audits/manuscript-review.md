# Manuscript-to-evidence audit
This audit compares the current manuscript with the implementation, preserved historical notebooks, configuration files, manuscript-transcribed results, and other evidence available in the ConceptSMILE repository.

Scientific methods, numerical tables, quantitative figures, and repository correspondence have been reviewed for traceability. No manuscript result values have been altered by this audit. Citation correctness across the entire external bibliography has not been independently re-audited here.

## Verified manuscript statements versus repository evidence

| Location | Current manuscript statement | Repository evidence / assessment |
| --- | --- | --- |
| Section 4.1, pp.13–14 | MedSAM and semantic VLM concept pathways | Preserved historical notebooks demonstrate both pathways, but they are exploratory single-image implementations rather than the complete four-dataset final manuscript pipeline. |
| Section 4.2, Eqs.3–6, pp.14–15 | Binary superpixel perturbations and original-minus-perturbed concept-response shift | Broadly supported by preserved code. Historical implementation details differ between pathways and should not automatically be treated as the final manuscript protocol. |
| Table 1, p.21 | 40 images, 10 per dataset; three concepts; 50 unique perturbations; SLIC target 7; black masking; DINOv2 CLS embeddings; cosine and Wasserstein locality; fixed structured VLM prompt; XGBoost surrogate | The author-confirmed 40-image evaluation identifiers are now documented in `data/manifests/paper_40_images.csv` and described in `data/manifests/README.md`. The preserved MedSAM legacy notebook still uses target 12, six realised segments, non-unique draws, and pooled MedSAM embeddings, so the historical implementation remains distinct from the manuscript-reported final protocol. |
| Section 4.3, Eq.9, p.16 | Exponential locality weighting, `exp(-d²/sigma²)` | Historical Wasserstein notebook code min-max normalises distance and uses `exp(-d_norm²/(2×0.75²))`. The historical implementation therefore contains operational details not established as the final paper configuration. |
| Section 4.3, Eq.10, p.16 | Weighted XGBoost regression of perturbation patterns against concept-response shifts | Repeated single-image XGBoost code is preserved. Complete final-paper hyperparameters, held-out split settings, and four-dataset execution provenance are not yet established from preserved evidence. |
| Section 4.4, Eq.11, pp.17–18; Table 3, p.26 | Attribution accuracy using reference labels | The final Table 3 evaluation used clinician reference annotations provided by Mehran Hosseinalizadeh (optometrist), produced independently of the model-generated outputs. Preserved legacy VLM and MedSAM notebooks contain exploratory model-derived/self-derived reference calculations and should not be treated as the source of the final Table 3 clinician-reference evaluation. |
| Section 4.4, Eqs.12–15, pp.18–19; Table 7, p.34 | WMSE, WMAE, R², and weighted R² surrogate fidelity | Reusable formula helpers implement the reported metric family for valid inputs, but preserved evidence does not independently reproduce the complete four-dataset Table 7. |
| Section 4.4, Eq.16, p.19; Table 4, p.27 | Concept-relevant perturbation strength versus absolute concept-response shift | Historical VLM code uses global removed fraction, while the MedSAM notebook uses predicted-mask affected fraction. Final row-level paper provenance remains required to establish the exact Table 4 calculation. |
| Section 4.4, Eq.17, p.19; Table 5, p.29 | Date/logo Jaccard stability | A reusable Jaccard helper exists, but the original explanation-set inputs and complete date/logo experiment used for Table 5 have not been recovered from the preserved historical notebooks. |
| Section 4.4, Eqs.18–19, pp.19–20; Table 6, p.31 | Variance and standard deviation of repeated concept-importance scores | Preserved historical code reports repeated R² dispersion rather than clearly documented repeated concept-importance statistics. Final Table 6 source records remain required. |
| Section 5.3, pp.35–37; Figs.10–11 | Robustness on a representative HRF image using contrast factors 0.6–1.4 and simulated occlusion levels 0–3% | The preserved MedSAM robustness notebook uses an ODIR image, while a complete preserved VLM robustness experiment has not been identified. The historical notebook should therefore not be relabelled as the HRF experiment reported in the paper. |
| Title page, p.1 | Seven named authors: Mohadeseh Mollapour, Koorosh Aslansefat, Zeinab Dehghani, Bhupesh Kumar Mishra, Tejal Shah, Zhibao Mian, and Mehran Hosseinalizadeh | Repository author metadata is aligned with the manuscript: `CITATION.cff` and `pyproject.toml` list all seven authors, including Mehran Hosseinalizadeh. |
| Section 6, pp.38–39 | Controlled proof-of-concept evaluation; no causal proof; no clinician-in-the-loop deployment or prospective clinical validation | The manuscript appropriately limits its claims. The use of retrospective clinician reference annotations for Table 3 does not constitute clinician-in-the-loop deployment or prospective clinical validation. These limitations do not by themselves establish provenance for numerical results, but they correctly bound the intended interpretation of the work. |

## Further evidence and implementation issues

1. **Table 4 locality dependence requires source confirmation.**  
   The preserved historical MedSAM and VLM faithfulness cells use ordinary Pearson correlation on strength/shift inputs without explicit locality weighting. Table 4 reports different correlation values under cosine and Wasserstein conditions. The original final calculation, sample selection, aggregation procedure, and row-level outputs should therefore be retained or recovered before claiming that the historical notebooks reproduce Table 4.

2. **Table 4 significance aggregation requires documentation.**  
   Historical code includes node-level p-value handling that does not by itself establish the aggregation procedure used in the manuscript table. The independent sample unit, aggregation level, standard-deviation calculation, and p-value procedure should be documented from the final experiment rather than inferred from legacy code.

3. **Table 6 scale and aggregation require source records.**  
   Several displayed variance/standard-deviation pairs cannot be interpreted confidently as a single repeated-score distribution without knowing the aggregation procedure. Separate averaging of variances and standard deviations across images or concepts could produce different relationships, but this must be established from the actual experiment records rather than reconstructed by assumption.

4. **Table 3/Table 7 repeated displayed values require source checking.**  
   Several displayed numerical pairs occur in both attribution and fidelity tables. Exact repetition is not proof of an error, but the final calculation outputs and table-assembly source should be retained so that the correspondence can be verified. The clinician-reference provenance of Table 3 resolves the reference-label interpretation issue but does not, by itself, establish numerical provenance for every displayed value.

5. **Figure 9 target definition requires final source data.**  
   The manuscript describes surrogate fidelity in terms of concept-response shifts, while historical exploratory plotting cells use different target representations in different places. The final Figure 9 data should establish explicitly whether the plotted quantity is concept-response shift, concept confidence, or confidence reconstructed from a predicted shift.

6. **Figure 11 provenance remains incomplete in the historical notebooks.**  
   The manuscript figure includes lesion, vessel, and optic-disc robustness. The preserved historical MedSAM robustness material does not unambiguously establish the complete final HRF figure source. The final figure-generating data and implementation should therefore be retained separately from the legacy notebook.

7. **Some final execution details remain undocumented in preserved evidence.**  
   The manuscript Table 1 documents the main experimental protocol, and the 40-image subset identifiers are now available in `data/manifests/paper_40_images.csv`. However, preprocessing details, kernel widths and any operational distance normalisation, final XGBoost hyperparameters, train/test split settings, repeat counts, exact model/checkpoint revisions, and the exact robustness image identifier remain to be established from the final experimental implementation where applicable.

## Current manuscript completion and repository-alignment items

- The previously missing APTOS and ODIR dataset citations are resolved in the current manuscript.
- The repository URL is present in the current Code Availability statement.
- The author-contribution section is completed in the current manuscript.
- The 40-image evaluation subset is now documented in `data/manifests/paper_40_images.csv`.
- The final Table 3 evaluation used clinician reference annotations provided by Mehran Hosseinalizadeh (optometrist), produced independently of model-generated outputs; the legacy model-derived/self-derived notebook calculations should not be treated as the final Table 3 reference-label source.
- Repository author metadata is aligned with the seven-author manuscript in both `CITATION.cff` and `pyproject.toml`.
- The manuscript title page assigns affiliation superscript `4` to Mehran Hosseinalizadeh, but affiliation 4 is not currently printed in the affiliation list. This should be completed using verified affiliation information.
- Section 2.3 currently contains the grammatical form `Vision language model provide`; this should be corrected to `Vision--language models provide`.
- Section 5.2.6 is still titled `Attribution Fidelity` even though the section defines and reports surrogate fidelity; the heading should be aligned with the manuscript terminology.
- The Limitations section currently says `multiple segmentation models and vision–language model`; the final noun should be plural.
- Confirm the aggregation unit used for tables reporting repeated or averaged results (for example image, concept, perturbation, or repeated run) and preserve that information alongside final row-level outputs.

## Required repository resolution order

1. Preserve the author-confirmed 40-image manifest as the canonical manuscript evaluation subset.
2. Keep repository author metadata aligned with the seven-author manuscript.
3. Preserve the legacy notebooks unchanged under `notebooks/legacy/`.
4. Preserve the distinction between the final Table 3 clinician-reference evaluation and the exploratory model-derived/self-derived attribution calculations contained in the legacy notebooks.
5. Add or recover the final manuscript implementation separately from the historical notebooks.
6. Retain final row-level outputs and figure-generation inputs for Tables 2–7 and Figures 9–11 where available.
7. Record final model/checkpoint revisions, preprocessing settings, locality parameters, surrogate settings, split strategy, and repeat counts where they were used.
8. Update repository traceability documents only when the supporting implementation or evidence is actually present.
9. Do not relabel historical exploratory outputs as final manuscript evidence merely because they resemble the reported results.
