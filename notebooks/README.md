# Final ConceptSMILE Implementation

This directory is reserved for implementation materials corresponding to the
current ConceptSMILE manuscript:

**ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI**

It is intentionally separated from the historical exploratory notebooks preserved
under `../legacy/`.

## Manuscript-aligned protocol

The current manuscript reports the following experimental protocol:

- four retinal fundus datasets: HRF, APTOS 2019, ODIR-5K, and IDRiD;
- 10 selected images from each dataset, giving 40 images in total;
- three retinal concepts: lesion, blood vessels, and optic disc;
- SLIC superpixels with a target of 7 segments;
- 50 unique binary superpixel perturbations per image;
- exclusion of the all-masked perturbation;
- black masking of removed superpixels;
- `facebook/dinov2-base` CLS-token embeddings for locality computation;
- cosine and Wasserstein distances;
- exponential locality weighting;
- a fixed structured JSON prompt for the VLM pathway; and
- XGBoost as the local surrogate model.

The author-confirmed evaluation image identifiers are recorded in:

`../../data/manifests/paper_40_images.csv`

The manuscript-reported experimental configuration is documented in:

`../../configs/paper.yaml`

## Relationship to historical notebooks

The notebooks stored under `../legacy/` are sanitised historical research
artefacts. They preserve exploratory source code and retained textual outputs but
do not constitute the complete implementation of the final 40-image manuscript
study.

Historical notebook settings differ from the manuscript-reported protocol in
several respects and are therefore retained separately for provenance.

The legacy notebooks must not be modified or relabelled merely to make them
appear to have generated the final manuscript results.

## Final implementation materials

Verified manuscript-aligned experiment notebooks, scripts, configuration files,
environment information, and related execution records may be added to this
directory when genuine supporting evidence is available.

Unknown historical or final execution settings must remain explicitly unknown
rather than being inferred from the legacy notebooks.

Any newly executed experiment should be clearly distinguished from the preserved
historical material and documented with its corresponding configuration,
environment, input manifest, and outputs.

## Reproducibility status

The reusable software under `../../src/conceptsmile/` implements and tests core
ConceptSMILE components, including perturbation, locality weighting, surrogate
modelling, reliability metrics, and robustness utilities.

However, a complete independently verified end-to-end rerun of the reported
four-dataset retinal experiments has not yet been established.

Accordingly, the repository distinguishes between:

1. the manuscript-reported protocol and results;
2. preserved historical notebooks under `../legacy/`;
3. reconstructed and tested reusable software under `../../src/conceptsmile/`;
4. manuscript-transcribed results under `../../results/manuscript_transcribed/`;
   and
5. verified final implementation material placed in this directory when available.

Manuscript-transcribed numerical results must not be described as computational
reproductions unless they are independently regenerated from a verified final
implementation and corresponding experimental records.
