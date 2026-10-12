
# Reviewed ConceptSMILE Manuscript

## Manuscript title

ConceptSMILE for Evaluating the Reliability of Concept Based Explainable Artificial Intelligence

## Latest manuscript

- File: `Moha___ConceptSMILE (6)(1).pdf`
- Length: 49 pages
- SHA-256: `a190164f2e40623283744e53a3860f407f9e110d4688eed1c6d25a660bd4464d`

## Experimental evaluation

The manuscript reports a controlled evaluation involving:

- Four retinal datasets: HRF, APTOS 2019, ODIR-5K, and IDRiD.
- 40 fundus images, with 10 images from each dataset.
- Three retinal concepts: lesion, blood vessels, and optic disc.
- Two concept-extraction pathways: MedSAM and Qwen2.5-VL.
- 50 unique binary superpixel perturbations per image.
- SLIC superpixels with target segments = 7.
- Black masking of removed superpixels.
- DINOv2 CLS-token embeddings for locality computation.
- Cosine and Wasserstein locality weighting.
- XGBoost surrogate modelling.

These are manuscript-reported settings, not a claim that all experiments have been independently reproduced.

## Results and provenance

Tables 2–7 are available in:

`results/manuscript_transcribed/`

Tables 3, 6, and 7 were synchronised with the revised manuscript using `Moha___ConceptSMILE (4)(5).pdf`, SHA-256:

`fe0dd95e208c25c4676413851fa97a995aba846b844f51b87ea0daa69ef9e460`

Their reported table values have also been checked against the latest manuscript listed above.

Tables 2, 4, and 5 retain their earlier manuscript-source records pending metadata synchronisation.

The CSV tables are manuscript transcriptions, not independently regenerated experimental results. Historical notebooks and reproducibility limitations are documented separately.

## Code availability

The associated code, preserved experimental materials, manuscript-reported results, and reproducibility documentation are available at:

https://github.com/MohadesehMollpour/ConceptSMILE

## Reproducibility statement

This repository distinguishes historical experimental evidence from reconstructed reusable implementations and documents remaining reproducibility limitations.
