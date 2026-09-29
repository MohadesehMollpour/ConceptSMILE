# Scientific provenance

Release scope: transparent research software and historical evidence record. This release does not by itself establish independent reproduction of all manuscript-reported results.

| Category | Meaning in this package |
| --- | --- |
| ORIGINAL | Authenticated original experiment artefact; originality is not established merely by presence in the repository |
| PRESERVED | Historical source cells/plain-text outputs retained; notebook derivatives are explicitly sanitised |
| RECONSTRUCTED | Reusable package utilities, input validation, audit scripts and tests; not original experimental execution |
| RE-RUN | Software-only tests/audits performed now; no new retinal/model experiment |
| MANUSCRIPT-TRANSCRIBED | Tables 2–7 and reported paper settings copied from the hashed PDF; no empirical reproduction implied |
| UNVERIFIED | Attribution of a result to original data/code remains unresolved |
| NOT AVAILABLE | Required artefact was not found among supplied materials |

## What the historical metrics mean

The historical notebook calculations described below are preserved exploratory evidence.
They should not automatically be interpreted as the implementations used to generate the
final manuscript results.

- **Final Table 3 clinician reference:** The final manuscript Table 3 evaluation used
  clinician reference annotations provided by Mehran Hosseinalizadeh (optometrist),
  produced independently of the model-generated outputs. These clinician reference
  annotations define the ground-truth basis reported for the final attribution evaluation.

- **Legacy VLM attribution:** Preserved VLM cells V12/18/23 contain a self-referential
  response-shift diagnostic with a positional label-alignment issue. V12 creates
  perturbation-major rows, while V18/23 generate labels in grouped concept order from
  the 75th percentile of those same scores. This historical diagnostic is not the
  clinician-reference evaluation used for the final Table 3 results.

- **Legacy MedSAM attribution:** Preserved MedSAM cells M30/38 compare response-shift
  scores with removal of at least 10% of an original model-predicted mask. This historical
  calculation represents model-mask-reference agreement and is not the clinician-reference
  evaluation used for the final Table 3 results.

- **VLM faithfulness:** Pearson association between global removed-superpixel fraction
  (V17) and absolute response shift (V25). The preserved historical implementation does
  not establish the exact final manuscript concept-specific calculation.

- **MedSAM faithfulness:** Historical calculations use the affected fraction of a
  model-derived mask. Node p-values averaged in M42 do not, by themselves, establish the
  final manuscript significance procedure.

- **Legacy consistency:** Preserved historical cells quantify dispersion of repeated-split
  R²/weighted R². No complete repeated concept-importance arrays corresponding to the
  final manuscript consistency analysis have been recovered from the preserved notebooks.

The reusable `evaluate_attribution` function accepts caller-provided reference labels.
It therefore supports externally supplied clinician annotations, but the function alone
does not establish the provenance of those labels.

The final Table 3 clinician-reference provenance is author-confirmed: the annotations
were provided by Mehran Hosseinalizadeh (optometrist) independently of the model-generated
outputs. Where available, the corresponding clinician annotation records, keyed mappings,
and row-level final evaluation outputs should be preserved separately from the legacy
notebook calculations.

## Preservation and sanitisation

Original notebook bytes remain in the prior private repository/archive at commit
`83a10462036a7b8de7ce356cf617a98d67357131`.

This repository includes sanitised notebook derivatives under `notebooks/legacy/`.
Source cells, execution counts, and plain-text numerical displays are preserved, while
non-text output payloads, attachments, and widgets were removed from the sanitised
notebook copies. Original/release hashes and removed locations are recorded in
`docs/audits/preservation_manifest.csv`. No sanitised derivative is claimed to be
byte-identical to its original notebook.

The manuscript framework and result figures are included under `figures/` for
documentation and traceability. Their inclusion does not establish independent
redistribution rights or experimental reproduction. Some figures contain retinal-image
content or other manuscript-derived graphical elements whose complete source provenance
and redistribution permissions have not been independently verified. Figure-specific
provenance limitations are documented in `figures/README.md`.

The original saved notebook output index is retained as an index of the historical
notebook outputs, not as a claim that removed MIME payloads remain in the repository.
Exact original provenance cannot be independently authenticated solely from notebook
metadata.

## Model/software evidence recovered

| Item | Evidence | Limits |
| --- | --- | --- |
| Python | Both `language_info` metadata records report Python 3.12.12 | Metadata, not a recovered full environment |
| PyTorch | M2 saved output reports PyTorch 2.8.0+cu126 and CUDA available `True` | CUDA build tag does not establish driver or hardware version |
| Hardware | V metadata reports accelerator `nvidiaTeslaT4` but `isGpuEnabled false`; M metadata reports no accelerator/GPU despite CUDA output | Contradictory metadata/output; actual historical hardware UNVERIFIED |
| MedSAM | M3 records checkpoint filenames `sam_vit_b_01ec64.pth` and `medsam_vit_b.pth`, Zenodo record 10689643; M5 reports zero missing/unexpected keys | Exact downloaded bytes, hash, and repository revision NOT AVAILABLE |
| Qwen | V3 records `Qwen2_5_VL` class, local directory `qwen25vl_3b_local`, float16, `device_map=auto`, and local processor | Exact model/tokenizer revision NOT AVAILABLE; directory name is not an authenticated model identifier |
| DINOv2 | V10 records `facebook/dinov2-base` and CLS extraction | Revision/checksum NOT AVAILABLE; M locality uses its image encoder rather than DINOv2 |
| Seeds | V8 uses `default_rng(42)`; M16 uses seed 42; repeated split cells use `42 + repeat`; M10 uses `random.seed(0)` for heuristic seed selection | Distinct stages use different seeds; there is no verified single universal paper seed |
| Packages | M2 requests OpenCV 4.9.0.80; V0/1/2 contain conflicting moving/pinned Transformers installation steps | No coherent historical lockfile; installation commands do not prove final resolved package versions |

Legacy settings remain separate from `configs/paper.yaml`. Missing values remain `null`.
Candidate model dependencies are not presented as a validated historical execution
environment.
