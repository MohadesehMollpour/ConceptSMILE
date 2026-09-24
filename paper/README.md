# Reviewed manuscript

**ConceptSMILE: Auditing the Trustworthiness of Concept-Based Explainable AI**

Current manuscript reviewed for repository alignment:

- File: `Moha___ConceptSMILE (16).pdf`
- Length: 49 pages
- SHA-256: `9178fc53e22cc259142915264e9d52c8d7769c6aa8ec820b10057d743d90470c`

The manuscript reports a 40-image retinal evaluation using 10 images from each
of HRF, APTOS 2019, ODIR-5K, and IDRiD. The author-confirmed image identifiers
are documented in `data/manifests/paper_40_images.csv`.

The manuscript reports the ConceptSMILE protocol using:

- three retinal concepts: lesion, blood vessels, and optic disc;
- 50 unique binary superpixel perturbations per image;
- SLIC superpixels with target segments = 7;
- black masking of removed superpixels;
- `facebook/dinov2-base` CLS-token embeddings;
- cosine and Wasserstein distance;
- exponential locality weighting;
- a fixed structured JSON prompt for the VLM pathway; and
- XGBoost as the local surrogate model.

Tables 2–7 currently remain stored under `results/manuscript_transcribed/`
as manuscript-reported values unless independently reproduced from preserved
row-level experimental outputs.

The repository URL reported in the manuscript is:

`https://github.com/MohadesehMollpour/ConceptSMILE.git`

The current manuscript contains the completed dataset citations, code
availability statement, and author-contribution section.
