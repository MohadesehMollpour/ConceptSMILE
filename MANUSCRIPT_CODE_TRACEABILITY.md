# Manuscript–code traceability

Repository release status: **AMBER**; scientific and reproducibility gaps remain unresolved.

The current 49-page manuscript identified in `paper/README.md` has been reviewed.
Manuscript statements are treated as verified **as reported**, not automatically verified
as historically executed.

Detailed manuscript/evidence correspondence is documented in
`docs/audits/manuscript-review.md`.

Historical notebook references used below are:

- **M** = `notebooks/legacy/medsam_odir_single_image_experiment.ipynb`
- **V** = `notebooks/legacy/vlm_odir_single_image_experiment.ipynb`

Cell indices are zero-based.

Plain-text outputs remain inside sanitised notebook derivatives. Rich/image outputs were
removed during sanitisation, with preservation information recorded in
`docs/audits/preservation_manifest.csv` and
`results/preserved/notebook_output_index.csv`.

`PRESERVED` means historical source/plain-text evidence retained. The notebook
derivatives are sanitised and are not claimed to be byte-identical authenticated
original experiment files.

Reusable implementations under `src/conceptsmile/` are classified as
`RECONSTRUCTED` unless otherwise documented.

No complete four-dataset retinal experiment has been independently `RE-RUN` as part
of this audit.

The author-confirmed manuscript evaluation subset is now documented separately in:

`data/manifests/paper_40_images.csv`

This resolves the previous uncertainty about the 40 evaluation image identifiers but
does not, by itself, establish complete historical execution provenance.

## Manuscript protocol versus preserved implementation

| Component / claim | Preserved implementation and configuration | Reusable / current repository evidence | Publication correspondence | Assessment |
| --- | --- | --- | --- | --- |
| Evaluation subset | Legacy notebooks contain individual ODIR examples rather than the complete four-dataset subset | `data/manifests/paper_40_images.csv` contains the author-confirmed 40-image evaluation subset: 10 images each from HRF, APTOS 2019, ODIR-5K, and IDRiD | Table 1, p.21 | AMBER: subset identifiers now documented; complete historical execution still not independently verified |
| Preprocessing | M0 uses long side 1024; V uses 384×384 resizing | No single verified final four-dataset loader currently establishes all manuscript preprocessing details | §4.1 and §4.5 | AMBER: pathway-specific historical preprocessing; final preprocessing details remain incomplete |
| SLIC target 7 | M16 requests 12 and retained output shows six realised segments; V7 requests/outputs 7 | `perturbation/superpixels.py`; `configs/paper.yaml` records manuscript target 7 | Table 1, p.21 | RED for legacy MedSAM correspondence: M does not implement the manuscript-reported target-7 protocol |
| 50 unique perturbations | M16 samples without demonstrated deduplication; V8 deduplicates perturbation vectors | `sample_binary_perturbations`; paper config records 50 unique vectors | Table 1, p.21 | RED for legacy M uniqueness; legacy notebook cannot be treated as final paper implementation |
| All-zero exclusion | M16/V8 historically repair an all-zero draw by retaining a region rather than clearly resampling until nonzero | Reconstructed sampler can enforce exclusion explicitly | Table 1, p.21 | AMBER: manuscript says all-masked perturbation excluded; legacy operational handling differs |
| Black masking | M16 and V8 black-mask removed regions | `apply_superpixel_perturbation` | Table 1, p.21 | Supported at method level |
| Concept extraction / response | M7–12 and M17–24 use MedSAM-related heuristic concept extraction; V4–6, V9 and V12 use structured semantic prompting/generated-token responses | `concepts/medsam.py` and `concepts/vlm.py` provide reusable helpers | §4.1–4.2 | AMBER: helper-level support exists, but complete final model adapters/revisions are not established |
| MedSAM model | M1–5 reference SAM ViT-B and `medsam_vit_b.pth`; saved load output reports zero missing/unexpected keys | Mask and pooled-embedding helpers retained | MedSAM pathway | AMBER: checkpoint filename is preserved, but exact historical bytes/hash/revision remain unavailable |
| Qwen model | V3 references local `qwen25vl_3b_local`, float16, automatic placement, and processor from the same local folder | Token-response parsing utilities retained | VLM pathway | AMBER: exact model/tokenizer/processor revisions remain unavailable |
| Fixed VLM prompt | Preserved VLM notebook contains structured prompting logic | Final prompt implementation has not yet been independently established as the exact four-dataset paper execution | Table 1, p.21 | AMBER: historical structured prompting exists; complete final execution provenance remains incomplete |
| DINOv2 CLS embedding | V10–11 use `facebook/dinov2-base` with CLS extraction; M25/M34 instead use pooled MedSAM image-encoder representations | `embeddings/dinov2.py`; `configs/paper.yaml` records DINOv2 CLS | Table 1, p.21 | RED for legacy M correspondence: common DINOv2 locality representation is not supported by the retained M notebook |
| Cosine locality | M25 uses a median-positive-distance width; V11 uses a fixed value of 0.25 | `locality/distances.py` | §4.3 | AMBER: historical pathways use different operational kernel settings |
| Wasserstein locality | M34 and V20 use one-dimensional Wasserstein comparison over embedding components and historical min-max scaling | `wasserstein_embedding_distance` and locality-weight helpers | §4.3 | AMBER: historical normalisation/kernel-width details are not fully specified by the manuscript |
| Locality kernel | Historical implementations include exponential distance weighting but with pathway-specific operational settings | `configs/paper.yaml` records manuscript equation `exp(-(distance**2)/(sigma**2))` | Eq.9, §4.3 | AMBER: broad formulation corresponds; exact final widths/normalisation remain unresolved |
| XGBoost surrogate | M27/M36/M45 and V14/V22/V27 contain XGBoost surrogate fitting; historical repeats use split seeds based on 42+repeat and test fraction 0.30 | `surrogate/xgboost_surrogate.py` and `metrics/fidelity.py` | Eq.10, §4.3 | AMBER: single-image historical evidence exists; final four-dataset hyperparameters and split procedure are not fully established |
| Attribution ACC/F1/AUROC | Legacy MedSAM and VLM notebooks contain exploratory model-derived/self-derived reference-label calculations and should not be treated as the final Table 3 implementation. | The final manuscript Table 3 evaluation used clinician reference annotations provided by Mehran Hosseinalizadeh (optometrist), produced independently of the model-generated outputs. `metrics/attribution.py` accepts externally supplied reference labels. | Table 3, pp.25–26 | Clinician-referenced final evaluation; legacy notebook attribution calculations are retained separately as historical exploratory evidence and do not define the final Table 3 reference labels. |
| Pearson faithfulness | M42 uses affected fraction of model-predicted masks; V17/V25 use overall removed-superpixel fraction | `metrics/faithfulness.py` | Table 4, p.27 | RED if historical VLM calculation is interpreted as concept-specific evidence removal; exact final Table 4 provenance remains incomplete |
| Stability / date and logo | No complete preserved date/logo experiment was located | `metrics/stability.py` provides a generic Jaccard helper | Table 5, p.29 | RED for reproduction: helper alone does not reproduce the manuscript artefact study |
| Consistency | M27/M36/M37 and V14/V22 report variance/SD of repeated R²-type surrogate metrics | `metrics/consistency.py` provides generic sample-statistics helpers | Table 6, p.31 | RED for historical correspondence: repeated concept-importance records supporting manuscript Eqs.18–19 have not been recovered |
| Contrast / blink robustness, MedSAM | M43 earlier and M44 corrected version contain contrast/occlusion evaluation; historical conditions span 0.6–1.4 contrast and 0–3% occlusion | `robustness/acquisition.py` provides artefact utilities | §5.3; Fig.11, p.37 | AMBER: preserved experiment uses ODIR rather than the representative HRF image reported in the manuscript; retained M44 summary also lacks complete optic-disc evidence |
| Contrast / blink robustness, VLM | V26 restores a model for a future robustness cell; V27 is a surrogate comparison rather than a complete robustness experiment | No complete preserved VLM robustness driver | §5.3; Fig.10, p.36 | RED for reproduction: model restoration is not evidence of the full reported robustness experiment |

## Additional historical implementation issue

V12 constructs `node_compare_df` in perturbation-major order, with concepts represented
within perturbations.

V18 and V23 iterate using `groupby(node_name)`, create labels concept-by-concept, and
then assign the resulting label sequence positionally to the original frame.

This introduces a row-alignment problem in addition to the self-referential nature of
the historical VLM attribution reference.

Therefore, saved historical AUROC values from these legacy notebook calculations must
not be interpreted as the source of the final manuscript Table 3 clinician-referenced
evaluation.

The final Table 3 attribution evaluation used clinician reference annotations provided
by Mehran Hosseinalizadeh (optometrist), produced independently of the model-generated
outputs. The historical notebook cells remain preserved unchanged as exploratory
evidence and should not be relabelled as the final Table 3 implementation.

Any future attribution implementation should preserve explicit keyed alignment between
the clinician reference labels and the corresponding evaluated regions or concepts.

## Publication result register

| Item | Current manuscript location / meaning | Preserved or current repository evidence | Provenance / reproduction status |
| --- | --- | --- | --- |
| Table 1 | §4.5, p.21; experimental protocol and reproducibility settings | `configs/paper.yaml`; author-confirmed `data/manifests/paper_40_images.csv`; legacy notebooks contain conflicting historical settings | MANUSCRIPT-TRANSCRIBED protocol; 40-image identifiers now documented; complete execution not independently verified |
| Table 2 | §5.2.1, p.24; surrogate/locality comparison | M45/V27 contain single-image surrogate comparisons that do not establish the four-dataset aggregate table | CSV remains MANUSCRIPT-TRANSCRIBED; original aggregate result bundle not recovered |
| Table 3 | §5.2.2, pp.25–26; concept-level attribution accuracy | Author-confirmed final evaluation used clinician reference annotations provided by Mehran Hosseinalizadeh (optometrist), independently of model-generated outputs. Legacy M30/M31/M38/M39 and V18/V23 calculations are historical exploratory implementations and are not the final Table 3 reference-label source. | Clinician-reference provenance confirmed by the authors; manuscript CSV remains MANUSCRIPT-TRANSCRIBED unless the corresponding row-level final evaluation records are separately preserved in the repository. |
| Table 4 | §5.2.3, p.27; faithfulness | M42/V25 contain historical Pearson calculations; preserved code does not establish the reported locality-dependent aggregate table | CSV MANUSCRIPT-TRANSCRIBED; final sample/aggregation/p-value provenance unresolved |
| Table 5 | §5.2.4, p.29; date/logo stability | Generic Jaccard helper exists; original explanation sets and complete experiment not recovered | CSV MANUSCRIPT-TRANSCRIBED; empirical reproduction not established |
| Table 6 | §5.2.5, p.31; repeated-run consistency | Historical notebooks contain R²-dispersion statistics rather than clearly documented repeated concept-importance arrays | CSV MANUSCRIPT-TRANSCRIBED with displayed scaling; final aggregation/source records unresolved |
| Table 7 | §5.2.6, p.34; surrogate fidelity | Historical single-image surrogate code exists but no complete four-dataset final output bundle has been recovered | CSV MANUSCRIPT-TRANSCRIBED; aggregate reproduction not established; repeated displayed pairs remain flagged for source checking |
| Figure 9 | §5.2.6, pp.32–33; observed versus surrogate-predicted concept-response shifts across four datasets | Historical exploratory M/V plots use mixed target handling; complete four-dataset plotting inputs are absent | Manuscript figure preserved for documentation; final point-level source data and exact target-generation pipeline remain unresolved |
| Figure 10 | §5.3, p.36; VLM robustness under contrast variation and simulated blink-related occlusion | V26 restores a model but does not contain the complete reported robustness experiment | Manuscript figure preserved; full driver and underlying result data not independently reproduced |
| Figure 11 | §5.3, p.37; MedSAM robustness under contrast variation and simulated blink-related occlusion | M43/M44 retained; preserved experiment uses ODIR, and M44 does not provide complete optic-disc evidence corresponding to the manuscript figure | Manuscript figure preserved; exact final HRF source image, execution version, and row-level data remain unresolved |
| Figures 1–8 | Conceptual, methodological, and qualitative figures preceding the quantitative result figures | Framework material and selected notebook-derived visual material are retained under `figures/` | Documentation/provenance available only to the extent recorded in `figures/README.md`; inclusion does not prove experimental reproduction or redistribution rights |

## Figure 9 target traceability

The current manuscript explicitly describes Figure 9 as comparing observed
concept-response shifts with values predicted by the local XGBoost surrogate.

The preserved historical notebooks do not provide one uniform plotting implementation
that can be confidently identified as the complete final Figure 9 source.

Historical VLM cells include both perturbed-confidence and response-shift target
treatments, while historical MedSAM plotting uses response shifts.

For this reason, the current manuscript interpretation is recorded as the reported
final specification, while the historical exploratory notebook implementations remain
separately documented rather than being relabelled as the final figure-generation code.

## Evaluation subset traceability

The manuscript reports:

- four datasets: HRF, APTOS 2019, ODIR-5K, and IDRiD;
- 10 images from each dataset;
- 40 retinal fundus images in total.

The author-confirmed identifiers are now stored in:

`data/manifests/paper_40_images.csv`

The manifest is linked from:

`configs/paper.yaml`

This resolves the earlier repository statement that the exact 40-image selection was
unavailable.

The manifest intentionally leaves `source_filename` blank where an exact original
filename or extension has not been independently verified.

The manifest should therefore be treated as the canonical author-confirmed evaluation
identifier list, not as independent proof that every historical notebook/output bundle
was executed against that exact subset.

## Current provenance interpretation

Table CSV files under:

`results/manuscript_transcribed/`

retain the values and precision reported in the manuscript.

They are not labelled as computed reproductions unless a genuine rerun and supporting
row-level outputs are subsequently added.

Framework and figure provenance are documented under `figures/`.

Metric interpretation, historical evidence limitations, and unresolved numerical
provenance are further documented in:

- `docs/scientific_provenance.md`
- `docs/audits/manuscript-review.md`
- `docs/audits/final-scientific-audit.md`
- `docs/reproducibility.md`

Individual **RED** assessments in the component table refer to specific scientific
traceability or historical-implementation conflicts. They do not change the separately
defined overall repository release status of **AMBER**.

## Current repository principle

The repository distinguishes three different things that must not be conflated:

1. **The manuscript-reported final protocol and results.**
2. **Historical exploratory notebook evidence preserved under `notebooks/legacy/`.**
3. **Reusable reconstructed code and the developing final implementation area.**

Legacy notebook settings must not be modified merely to make them appear to have
generated the manuscript results.

Final manuscript implementation should instead be stored separately under
`notebooks/final/` and should follow the manuscript-reported protocol.

Where final execution settings or source records are unknown, they must remain explicitly
unknown until genuine evidence is recovered.

The author-confirmed 40-image manifest may be used as the final evaluation subset
reference, but it does not convert legacy single-image notebooks into verified
four-dataset manuscript reproductions.
