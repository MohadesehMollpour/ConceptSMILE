# ConceptSMILE

A perturbation-based approach to auditing concept-level explanation reliability: mask image regions, measure concept-response shifts, compute locality weights and fit a local surrogate.

**AMBER: transparent research release with incomplete historical reproducibility.** This package contains reusable reconstructed utilities, sanitised historical evidence and explicitly labelled manuscript transcriptions. It does not reproduce the full paper or validate its disputed comparative results. Start with [FINAL_REPOSITORY_STATUS.md](FINAL_REPOSITORY_STATUS.md).

## ConceptSMILE framework

<p align="center">
  <img
    src="figures/framework/figure04_conceptsmile_framework_overview.png.png"
    alt="Overview of the ConceptSMILE framework"
    width="100%"
  >
</p>

<p align="center">
  <em>Overview of the ConceptSMILE framework. The pipeline extracts concept-level outputs,
  applies controlled superpixel perturbations, computes locality weights, and fits a local
  surrogate model for reliability auditing.</em>
</p>

## Evidence you can inspect

- MedSAM and Qwen2.5-VL notebooks each demonstrate one image from an ODIR mirror. Source cells and plain-text outputs are preserved; embedded visuals/rich displays are removed with an [audit trail](docs/audits/preservation_manifest.csv).
- The manuscript evaluation uses 40 retinal fundus images across HRF, APTOS 2019, ODIR-5K, and IDRiD, with 10 images from each dataset. The author-confirmed image identifiers are documented in the [evaluation image manifest](data/manifests/README.md) and provided in machine-readable form in [`paper_40_images.csv`](data/manifests/paper_40_images.csv).
- [Tables 2–7](results/manuscript_transcribed/README.md) are MANUSCRIPT-TRANSCRIBED, not computed reproductions.
- Historical MedSAM reference metrics mean **model-mask-reference agreement**. VLM attribution is a **self-referential, row-misaligned diagnostic**, not independent ground-truth accuracy. VLM Pearson uses global removed fraction, and legacy consistency measures R² dispersion. These limitations remain unresolved scientifically.
- Stability, full VLM robustness, four-dataset row-level outputs and exact Figure9–11 provenance are incomplete. Table arithmetic/duplication concerns are documented in the [final scientific audit](docs/audits/final-scientific-audit.md).

## Install and check

Python 3.10 or later, from this repository root:

```bash
python -m pip install -e .[dev]
python -m pytest
python -m conceptsmile
python scripts/synthetic_smoke_test.py
python scripts/validate_config.py configs/paper.yaml
python scripts/audit_manuscript_tables.py
