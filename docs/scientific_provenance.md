# Scientific provenance

Release scope: transparent research software and historical evidence record. This release does not validate disputed manuscript results.

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

- **VLM attribution:** self-referential response-shift diagnostic with a positional label-alignment error. V12 creates perturbation-major rows; V18/23 generate labels in grouped concept order from the 75th percentile of those same scores. Not independent attribution accuracy. Independent labels are NOT AVAILABLE.
- **MedSAM attribution:** agreement between response-shift scores and removal of at least 10% of an original predicted mask (M30/38). This is model-mask-reference agreement, not clinician or dataset ground truth. The masks originate from MedSAM heuristic prompting, not imported reference annotations.
- **VLM faithfulness:** Pearson association between global removed-superpixel fraction (V17) and absolute response shift (V25). It is not measured concept-specific evidence removal.
- **MedSAM faithfulness:** correlation with the affected fraction of a model-derived mask. Node p-values averaged in M42 do not constitute a combined significance test.
- **Legacy consistency:** dispersion of repeated-split R²/weighted R². No genuine repeated concept-importance arrays were supplied. The generic sample-variance helper is not recovery of those missing data.

The reusable `evaluate_attribution` function accepts caller-provided labels and cannot establish their independence. Its name does not validate historical metrics. Independent annotations with verifiable provenance and correctly keyed alignment are required for a new attribution evaluation.

## Preservation and sanitisation

Original notebook bytes remain in the prior private repository/archive at commit 83a10462036a7b8de7ce356cf617a98d67357131. This ZIP includes sanitised derivatives under notebooks/legacy. Source cells, execution counts and plain-text numerical displays are preserved; non-text output payloads, attachments and widgets are omitted. Original/release hashes and removed locations are in audits/preservation_manifest.csv. No original is claimed to be byte-identical to its derivative. The framework raster is omitted, but its hash and confirmed correspondence to PDF Figure 4 remain recorded.

The original saved notebook output index is retained as an index of the original, not as a claim that removed MIME payloads remain in the package. Exact original provenance cannot be independently authenticated solely from notebook metadata.

## Model/software evidence recovered

| Item | Evidence | Limits |
| --- | --- | --- |
| Python | Both language_info metadata report 3.12.12 | Metadata, not a recovered full environment |
| PyTorch | M2 saved output 2.8.0+cu126 and CUDA available True | CUDA build tag does not establish driver/hardware version |
| Hardware | V metadata accelerator nvidiaTeslaT4 but isGpuEnabled false; M metadata accelerator none and GPU disabled despite CUDA output | Contradictory metadata/output; actual historical hardware UNVERIFIED |
| MedSAM | M3 checkpoint filenames sam_vit_b_01ec64.pth, medsam_vit_b.pth; Zenodo record 10689643; M5 zero missing/unexpected keys | Exact downloaded bytes/hash and repository revision NOT AVAILABLE |
| Qwen | V3 Qwen2_5_VL class, qwen25vl_3b_local, float16, device_map auto, local processor | Exact model/tokenizer revision NOT AVAILABLE; directory name is not authenticated model ID |
| DINOv2 | V10 facebook/dinov2-base and CLS extraction | Revision/checksum NOT AVAILABLE; M locality uses its image encoder, not DINOv2 |
| Seeds | V8 default_rng(42); M16 seed42; repeated split cells 42+repeat; M10 random.seed(0) for heuristic seed selection | Distinct stages; not one universal paper seed |
| Packages | M2 requests OpenCV 4.9.0.80; V0/1/2 contain conflicting moving/pinned Transformers installs | No coherent historical lock; install command is not proof of final resolved versions |

Legacy settings stay separate from configs/paper.yaml. Missing values remain null. Candidate model dependencies are not a validated execution environment.
