# Manuscript–code traceability

Repository release status: **AMBER**; scientific discrepancies remain unresolved. The 46-page manuscript identified in `paper/README.md` has now been reviewed. Manuscript statements are verified as reported, not verified as executed. Detailed page/equation correspondence and new discrepancies are in `docs/audits/manuscript-review.md`. M = `notebooks/legacy/medsam_odir_single_image_experiment.ipynb`; V = `notebooks/legacy/vlm_odir_single_image_experiment.ipynb`. Cell indices are zero-based. Plain-text outputs remain inside sanitised notebook derivatives; rich/image outputs were omitted with hashes and are indexed in `results/preserved/notebook_output_index.csv`.

PRESERVED means historical source/plain-text evidence retained; notebook derivatives are sanitised and not byte-identical to originals, not independently authenticated ORIGINAL code. All reusable `src/conceptsmile/` implementations are RECONSTRUCTED, including inherited code. No retinal results are RE-RUN in this audit.

| Component / claim | Preserved implementation and configuration | Reusable implementation | Inputs → outputs / publication correspondence | Assessment |
| --- | --- | --- | --- | --- |
| Preprocessing | M0 long side 1024; V image resized 384×384; legacy YAML | No unified loader | ODIR mirror image1/image1001 → image arrays; §4.1/4.5, pp.13–14/20–21 | AMBER: pathway-specific; four-dataset pipeline absent |
| SLIC target 7 | M16 requests 12, output 6; V7 requests/output 7 | perturbation/superpixels.py | Image → label map; Table 1 p.21; paper.yaml manuscript-reported | RED: M conflicts with requested paper protocol |
| 50 unique perturbations | M16 no deduplication; V8 deduplicates | sample_binary_perturbations | Region count → binary keep vectors | RED for M uniqueness; actual SLIC count must permit 50 states |
| All-zero exclusion / black masking | M16, V8 retain one region after zero draw and black-mask removed regions | sampler and apply_superpixel_perturbation | Vector → masked image | AMBER: preserved protocol; not uniform rejection sampling |
| Concept extraction / response | M7–12,17–24 heuristic prompts, mean mask probability; V4–6,9,12 fixed prompt and generated-token probabilities | concepts/medsam.py and vlm.py are helpers only | Original and perturbed responses → shifts | AMBER: no verified complete adapter or model revisions |
| MedSAM model | M1–5 SAM vit_b then medsam_vit_b.pth; strict=False output zero missing/unexpected | Mask and pooled-embedding helpers | Checkpoint file → masks; hash unknown | AMBER: known filename is not checkpoint authentication |
| Qwen model | V3 local qwen25vl_3b_local, float16, auto placement; processor from same folder | Token parser | Generated answer token → probability heuristic | AMBER: no exact checkpoint/tokenizer revision; 1−P(no) is not calibrated P(yes) |
| DINOv2 CLS | V10–11 facebook/dinov2-base; M25/34 use pooled MedSAM encoder | embeddings/dinov2.py | Images → embeddings | RED: common embedding claim not supported for M |
| Cosine locality | M25 median positive distance width; V11 fixed 0.25 | locality/distances.py | Embeddings → 1−cosine, exp(−d²/sigma²) | AMBER: pathway-specific settings |
| Wasserstein locality | M34; V20, one-dimensional distribution of embedding components | wasserstein_embedding_distance / locality_weights | Distances min-max scaled → exp(−d²/(2×0.75²)) | AMBER: component distributions discard coordinate matching; not spatial transport |
| XGBoost / fidelity | M27,36,45; V14,22,27, repeat splits 42+repeat, 30 repeats, test fraction .30 | surrogate/xgboost_surrogate.py; metrics/fidelity.py | Keep vectors and response shifts → held-out prediction metrics | AMBER: notebook single-image evidence, not four-dataset aggregates |
| Attribution ACC/F1/AUROC | M30/38 labels affected original predicted-mask fraction ≥.10; V18/23 labels same-score 75th percentile | metrics/attribution.py requires supplied labels | Reference and score → metrics | RED: V circular and misaligned; M masks model-derived, not independent expert ground truth; same-sample threshold optimisation |
| Pearson faithfulness | M42 uses predicted-mask affected pixels; V17/25 overall fraction of removed superpixels | metrics/faithfulness.py | Affected fraction and absolute shift → correlation | RED if V described as concept-specific; M reference also model-dependent; mean node p-values not a combined significance test |
| Stability / date and logo | No experiment located | metrics/stability.py Jaccard helper only | Explanation-set inputs absent; Table 5 p.29 | RED: helper does not reproduce artefact study |
| Consistency | M27/36/37; V14/22: variance/std of R² and weighted R² | metrics/consistency.py generic sample statistics | Repeated scores → variance/std | RED: no repeated importance-score provenance |
| Contrast / blink robustness, M | M43 earlier, M44 labelled corrected with saved summary/figures; legacy conditions .6–1.4 and 0–3% | robustness/acquisition.py artefact utilities only | ODIR single image → repeated Test R²; row-level CSV paths printed, files absent | AMBER: preserved display, not authenticated publication plot; optic-disc rows absent in M44 summary |
| Contrast / blink robustness, V | V26 restores model for a future robustness cell; V27 is surrogate comparison | No full VLM robustness driver | Result inputs unavailable | RED: restoration cell is not robustness experiment |

## Additional implementation issue

V12 constructs `node_compare_df` in perturbation-major order (three concepts per perturbation). V18 and V23 iterate `groupby(node_name)` and append labels concept by concept, then assign the list positionally to the original frame. This breaks row alignment in addition to the circular reference definition. Saved AUROC values below 1 must not be interpreted as resolving circularity. Historical cells remain untouched; independent labels and correctly keyed alignment are required for a new evaluation.

## Publication result register

| Item | Manuscript location and meaning | Preserved evidence | Provenance / reproduction status |
| --- | --- | --- | --- |
| Table 1 | §4.5, p.21 protocol | Legacy configs differ | MANUSCRIPT-TRANSCRIBED into paper.yaml; execution not verified |
| Table 2 | §5.2.1, p.23 surrogate selection | M45/V27 single-image displays differ from aggregate table | CSV MANUSCRIPT-TRANSCRIBED; original aggregate bundle missing |
| Table 3 | §5.2.2, p.25 attribution | M30/31/38/39, V18/23; reference defects | CSV MANUSCRIPT-TRANSCRIBED; RED empirical validity/provenance |
| Table 4 | §5.2.3, p.27 Pearson faithfulness | M42/V25; no weighted correlation; aggregate provenance absent | CSV MANUSCRIPT-TRANSCRIBED; RED locality/p-value interpretation |
| Table 5 | §5.2.4, p.29 date/logo stability | No original set inputs or experiment | CSV MANUSCRIPT-TRANSCRIBED; RED missing provenance |
| Table 6 | §5.2.5, p.31 consistency | R² statistics differ from Eqs.18–19 importance semantics | CSV MANUSCRIPT-TRANSCRIBED with displayed scaling; RED |
| Table 7 | §5.2.6, p.34 fidelity | Single-image code, no four-dataset source bundle | CSV MANUSCRIPT-TRANSCRIBED; RED aggregate provenance; repeated table pairs flagged |
| Figure 9 | §5.2.6, p.32 four-dataset actual/predicted fidelity panels | Exploratory M/V plots; full panel data absent | PRESERVED manuscript figure; target confidence/shift ambiguity; no numerical reconstruction |
| Figure 10 | §5.3, p.35 VLM robustness | V26 model restoration is not full experiment | PRESERVED manuscript figure; RED missing driver/data |
| Figure 11 | §5.3, p.35 MedSAM robustness | M43/44 retained; M44 lacks plotted optic-disc results | PRESERVED manuscript figure; exact source version/HRF identity unresolved |
| Figures 1–8 | pp.4,6,8,13,14,17,18,22 conceptual/qualitative figures | One framework raster plus notebook images | Latest publication locations verified; generation/source provenance incomplete |

Table CSVs in `results/manuscript_transcribed/` retain published precision and all questionable entries. They are not computed reproductions. Framework raster matching and figure provenance are described in `figures/framework/README.md`. No figure was digitised to invent point-level results.

Current exact metric labels and resolution of Figure9 target candidates are in docs/scientific_provenance.md and docs/audits/final-scientific-audit.md. Red cells in the component table concern scientific evidence, not the separately assessed AMBER package scope.
