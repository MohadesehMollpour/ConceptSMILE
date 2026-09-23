# Final scientific audit

**Repository release status: AMBER.** The package is suitable as a transparent, limited research release under its existing rights statement. This does not make disputed results scientifically valid or the manuscript submission-ready. Earlier RED decisions applied to the unqualified reproduction/release claim and unsanitised imagery. This package removes those claims/assets and discloses remaining evidence gaps; it does not hide or repair historical results.

Base compared read-only to live submission-ready: 83a10462036a7b8de7ce356cf617a98d67357131. No new named `(1).zip` was attached, so the current local repository and previously produced archive were used and compared with that live branch. Latest PDF: SHA-256 c4a9c68fe7ae240530a6db9a3509d4116d94cd59976fec259b6ec71d2d87d992.

| Requested issue | Investigation / outcome | Remaining evidence gap |
| --- | --- | --- |
| 1 VLM labels | V12/18/23: same-score 75th percentile plus group/row order mismatch; labelled self-referential diagnostic | Independent labels NOT AVAILABLE; no historical number changed |
| 2 MedSAM references | M10–12/30/38: predicted masks; labelled model-mask-reference agreement | No clinician/dataset annotation provenance |
| 3 MedSAM protocol | M16 target12/realised6, 50 nonunique draws, zero-vector repair, black masking, seed42; M25/34 global-average pooled per-image MedSAM encoder; random 30% held-out split | Does not implement common DINOv2/target7/unique paper protocol; duplicate patterns can cross splits |
| 4 VLM faithfulness | V17/25 uses global removed fraction; reusable correlation described neutrally | No concept-specific affected evidence |
| 5 Consistency | M27/36/37,V14/22 use R² variation | Importance-score run data NOT AVAILABLE |
| 6 Table6 arithmetic | Every one of 48 pairs in table6_variance_sd_audit.csv | 1 printed-rounding compatible, 43 possible coarser rounding, 4 inconsistent even under coarser assumption; aggregation unresolved |
| 7 Table4 provenance | 144 value entries in table4_value_traceability.csv; numeric matches are not ancestry | Ordinary Pearson code has no locality weighting; raw aggregate CSV/arrays NOT AVAILABLE |
| 8 Cross-table values | All exact displayed scalar matches in cross_table_exact_value_matches.csv | Intentional reuse/copying cannot be determined; highlighted paired matches remain suspicious |
| 9 Figure9 target | V13/15 fits/plots perturbed confidence in-sample; V21 fits shifts; M26/29 fits/plots shifts | Full four-dataset Figure9 source absent; mixed historical targets mean global figure target cannot be resolved |
| 10 Robustness | M43/44 code and text outputs; 30 split repeats in full mode, 3 fast mode; M44 output FAST_TEST False. M44 averages nodes within concept/repeat then pandas mean/median/sample SD across repeats | Figure11 has optic-disc curves absent from corrected M44; M image is ODIR vs paper HRF; V26 only restores model, no V robustness experiment |
| 11 Stability | Searched both sources/outputs for date/logo/Jaccard experiment; no supporting implementation/sets | Table5 manuscript-only; no NHS logo asset packaged |
| 12 Manifest | Only ODIR mirror image1/image1001 names recovered; no full selection list | No fabricated paper_40_images.csv |
| 13 Models/software | Metadata, saved version strings, checkpoint names, seeds and conflict documented in scientific_provenance.md | Model hashes, coherent environment and actual hardware unresolved |
| 14 Images/privacy | 13 original PNG output objects reviewed; retinal visualisations and plots. Source code points to public ODIR mirror, exact official IDs unverified. Non-text payloads/framework raster omitted | Rights not presumed; historical originals retained privately with hashes |
| 15 Licence | Existing all-rights-reserved notice retained | Author licence decision required for reuse rights; no open-source claim |
| 16 Citation | Six CFF authors match PDF p1 | No final publication details invented |
| 17 Datasets | Provider links and retrieval/access limitations documented | No dataset redistribution or new annotation mapping |
| 18 Security | Current final tree including sources, plain-text outputs and metadata scanned; no confirmed secret found | Full Git history not scanned; making existing private repository public exposes history and is outside package review |
| 19 Code | Fractional labels/masks not truncated; empty and invalid-weight paths tightened; tests recorded | Model-heavy execution not performed |
| 20 Structure | Small source package, sanitised evidence, table transcriptions, audit scripts | No empty rerun results or simulated results added |
| 21 README | Rewritten around release scope and exact evidence meaning | Scientific limitations prominently retained |
| 22 Reproducibility | No claim of full/end-to-end paper reproduction or clinical validation | Historical gaps remain; new reruns must be separated |

## Table6 interpretation

Strict test uses half a printed last digit (0.00005) in each displayed column with variance×10^-4 and SD×10^-3. Secondary test allows variance rounded to two decimals then padded to four (half-unit .005×10^-4), while retaining printed SD precision. That is an explicit hypothetical rounding convention, not recovered evidence. The four severe pairs are MedSAM APTOS lesion and ODIR optic disc under both distances. Separate aggregation of SD and variance can also affect the relation and must be established from original records. The CSV sqrt column is a diagnostic, NEVER a proposed correction.

## Required manuscript corrections/recovery

See manuscript-review.md for page-specific detail: attribution reference claims; global versus concept-specific Pearson meaning and Table4 locality/significance; R² dispersion versus importance consistency; Table6 scales; repeated Table3/7 metric pairs; Figure9 target; HRF/ODIR robustness identity; Table1 operational omissions/citations and pp40–41 placeholders. No manuscript source was edited. Recover row-level results before changing values. Documentation-only honesty cannot validate the paper's comparative conclusions.

Original annotations, raw CSVs, checkpoint files and dataset image IDs were searched in all supplied repository files and notebook source/text outputs; none sufficient to resolve the listed gaps was recovered. Public HRF annotations could support a new study only after verified sample matching, not historical reconstruction by assumption.
