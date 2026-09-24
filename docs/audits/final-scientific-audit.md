# Final scientific audit

**Repository release status: AMBER.** The repository is suitable as a transparent,
limited research release under its existing rights statement. This status means that
the repository clearly distinguishes manuscript-reported results, preserved historical
material, reconstructed utilities, and evidence gaps. It does not by itself establish
independent reproduction of every numerical result reported in the manuscript.

The current manuscript reviewed for repository alignment is:

- `Moha___ConceptSMILE (16).pdf`
- 49 pages
- SHA-256: `9178fc53e22cc259142915264e9d52c8d7769c6aa8ec820b10057d743d90470c`

The original repository audit was based on commit
`83a10462036a7b8de7ce356cf617a98d67357131`. The repository has since been
updated to document the author-confirmed 40-image evaluation subset, align author
metadata with the seven-author manuscript, and distinguish the final manuscript
implementation area from preserved legacy notebooks.

No manuscript numerical result has been silently altered as part of these repository
documentation updates.

| Requested issue | Investigation / current outcome | Remaining evidence gap |
| --- | --- | --- |
| 1 VLM labels | Preserved VLM cells V12/18/23 contain same-score percentile labelling together with group/row-order concerns. Historical outputs remain labelled as a self-referential diagnostic rather than independent ground truth. | Independent attribution labels are not established from the preserved historical material. |
| 2 MedSAM references | Preserved MedSAM cells M10–12/30/38 use predicted/model-derived masks as references. Repository documentation now describes these as model-mask-reference agreement rather than independent clinical annotation. | Independent clinician or dataset-annotation provenance is not established for the preserved historical calculation. |
| 3 MedSAM legacy protocol | Preserved MedSAM code uses target 12 SLIC segments, six realised segments in the retained example, non-unique perturbation draws, zero-vector repair, black masking, and pooled MedSAM image embeddings. | The preserved legacy notebook is not the final manuscript implementation of the reported common target-7, unique-perturbation, DINOv2 protocol. It remains intentionally separated under `notebooks/legacy/`. |
| 4 VLM faithfulness | Preserved VLM faithfulness code uses global removed fraction. Repository documentation now distinguishes this historical implementation from the manuscript-level concept-relevance description. | Final row-level evidence is required to establish the exact concept-specific calculation used for manuscript Table 4. |
| 5 Consistency | Preserved historical cells M27/36/37 and V14/22 quantify variation in R²-type surrogate measures. | Row-level repeated concept-importance outputs supporting the manuscript consistency definition have not been established from the preserved notebooks. |
| 6 Table 6 arithmetic | `table6_variance_sd_audit.csv` records all 48 displayed variance/SD pairs. The audit identifies one pair compatible with the strict printed-rounding interpretation, 43 potentially compatible under coarser rounding/aggregation assumptions, and four pairs requiring further source clarification. | The final aggregation rule and original repeated-score records remain necessary to interpret the displayed variance and SD values conclusively. |
| 7 Table 4 provenance | `table4_value_traceability.csv` records 144 displayed values. Preserved ordinary Pearson code does not itself explain different cosine/Wasserstein correlation values. | Final row-level arrays, sample-selection logic, aggregation procedure, and significance calculation are still required for full provenance. |
| 8 Cross-table values | Exact displayed scalar matches are recorded in `cross_table_exact_value_matches.csv`. Repeated values are treated as a traceability flag rather than proof of error. | Original result-generation and table-assembly records are required to determine whether repeated displayed values are intentional or mapping/copying artefacts. |
| 9 Figure 9 target | Historical VLM cells include both confidence-based and shift-based surrogate targets; preserved MedSAM plotting uses shifts. | Final four-dataset Figure 9 source data are needed to establish the exact plotted target consistently across manuscript panels. |
| 10 Robustness | Preserved MedSAM robustness cells M43/44 contain repeated contrast/occlusion evaluation logic. The preserved example uses an ODIR image, whereas the manuscript reports a representative HRF image. The retained VLM material does not contain a complete corresponding robustness driver. | Final HRF robustness image identity, row-level robustness outputs, and complete VLM robustness provenance remain to be documented from the final implementation/evidence. |
| 11 Stability | Historical material was searched for the date/logo/Jaccard experiment. A generic Jaccard implementation is available, but the complete original stability experiment and explanation sets have not been recovered from the preserved notebooks. | Final Table 5 input explanation sets and experiment records remain required for independent reproduction. |
| 12 Evaluation manifest | The author-confirmed 40-image evaluation subset is now documented in `data/manifests/paper_40_images.csv`, with 10 images each from HRF, APTOS 2019, ODIR-5K, and IDRiD. `configs/paper.yaml` links to this manifest. | The subset-identifier gap is resolved. Exact source filenames remain blank where they have not been independently verified, and the manifest alone does not establish complete historical execution provenance. |
| 13 Models/software | Available metadata, historical version strings, checkpoint names, seeds, and configuration differences are documented where recoverable. Unknown paper-level settings remain `null` rather than being invented. | Final checkpoint hashes/revisions, complete historical environment, hardware details, and other unavailable execution settings remain unresolved unless genuine records are recovered. |
| 14 Images/privacy | Historical retinal visualisations and plots were reviewed during the earlier audit. Source datasets are not redistributed in the repository, and current documentation directs users to obtain datasets independently. | Rights for any historical or third-party image material should not be presumed beyond documented sources. |
| 15 Licence | The existing all-rights-reserved notice is retained. | A separate author decision is required before describing the repository as open source or granting broader software reuse rights. |
| 16 Citation/authors | `CITATION.cff` and `pyproject.toml` now list all seven manuscript authors: Mohadeseh Mollapour, Koorosh Aslansefat, Zeinab Dehghani, Bhupesh Kumar Mishra, Tejal Shah, Zhibao Mian, and Mehran Hosseinalizadeh. | Final publication metadata such as journal citation, DOI, and publication date should be added only when confirmed. |
| 17 Datasets | HRF, APTOS 2019, ODIR-5K, and IDRiD are documented together with provider/retrieval guidance. The repository does not redistribute the datasets. | Dataset acquisition and any annotation mapping remain external to the repository unless separately documented. |
| 18 Security | Earlier current-tree scans found no confirmed credential secret in the reviewed package. | This is not equivalent to a complete Git-history security audit. Repository history should be reviewed separately before any visibility change. |
| 19 Code | Reusable reconstructed utilities include perturbation, locality, surrogate, and metric functionality with defensive validation for invalid/degenerate inputs. | Model-heavy four-dataset execution has not been independently rerun as part of this audit. |
| 20 Structure | Repository structure separates reconstructed source utilities, preserved legacy notebooks, manuscript-transcribed results, audit records, and a dedicated `notebooks/final/` area for the final manuscript implementation. | Final implementation notebooks and final experimental outputs should be added only when genuinely verified against the manuscript experiments. |
| 21 README | The root README now documents the 40-image manifest, legacy/final notebook distinction, repository scope, evidence meaning, and scientific limitations. | README claims should continue to be updated only when supporting evidence is added. |
| 22 Reproducibility | The repository does not claim that legacy notebooks reproduce the complete paper end-to-end. Manuscript-reported values remain clearly labelled where independent reproduction has not been established. | A complete final implementation plus row-level outputs, model/configuration records, and figure/table generation inputs are still needed for full end-to-end reproduction. |

## Table 6 interpretation

The arithmetic audit uses the scale factors printed in the manuscript:
variance ×10^-4 and standard deviation ×10^-3.

The strict diagnostic checks whether each displayed variance/SD pair could represent
the same underlying repeated-score distribution within the precision implied by the
printed values. A secondary diagnostic considers whether coarser rounding or separate
aggregation could explain additional pairs.

These diagnostics are **not proposed corrections to the manuscript values**.

The remaining discrepancies must be interpreted using the actual aggregation procedure
and source repeated-score records. In particular, averaging variances and standard
deviations separately across images, concepts, or repeated runs can break the simple
display-level relationship `SD = sqrt(variance)`. The repository therefore records the
issue without automatically changing the manuscript values.

## Current manuscript and repository alignment

The following earlier completion issues have now been resolved:

- the manuscript identifies all four retinal datasets with citations;
- the Code Availability section contains the ConceptSMILE repository URL;
- the Author Contributions section is completed;
- the author-confirmed 40-image evaluation subset is documented in
  `data/manifests/paper_40_images.csv`;
- `configs/paper.yaml` links to the evaluation manifest;
- `CITATION.cff` lists all seven manuscript authors;
- `pyproject.toml` lists all seven manuscript authors; and
- the root README documents the current manifest and separates historical notebooks
  from the final manuscript implementation area.

The following manuscript/editorial items remain visible in the current reviewed PDF
and should be resolved in the manuscript itself rather than by altering repository
evidence:

1. Mehran Hosseinalizadeh is marked with affiliation superscript `4`, but affiliation 4
   is not printed in the title-page affiliation list. Add the verified affiliation only
   when its exact wording is confirmed.

2. Section 2.3 contains:
   `Vision language model provide`
   and should be grammatically corrected to:
   `Vision–language models provide`.

3. Section 5.2.6 is titled `Attribution Fidelity`, although the section itself discusses
   surrogate fidelity. The heading should be aligned with the terminology used in the
   section.

4. The Limitations section contains:
   `multiple segmentation models and vision–language model`
   and should use the plural:
   `multiple segmentation models and vision–language models`.

These are manuscript-language or metadata corrections; they do not require changes to
the reported numerical results.

## Evidence still required for complete reproduction

The author-confirmed image manifest resolves the earlier uncertainty about which
40 image identifiers belong to the manuscript evaluation. It does **not**, by itself,
resolve the remaining result-provenance questions.

For complete end-to-end reproducibility, the repository should eventually contain or
document, where genuinely available:

- the final manuscript implementation for both MedSAM and VLM pathways;
- final preprocessing details;
- exact model/checkpoint revisions or hashes;
- final locality kernel widths and any distance normalisation;
- final XGBoost hyperparameters;
- train/test or validation split procedure;
- repeat counts and aggregation rules;
- final row-level outputs for the four datasets;
- final source records supporting Tables 2–7;
- Figure 9 plotting inputs and target definition;
- Table 5 stability explanation sets/results;
- Table 6 repeated concept-importance records;
- Figures 10–11 robustness inputs and the exact HRF robustness image identifier; and
- complete environment information sufficient to rerun the final experiments.

Unknown values should remain explicitly unknown rather than being inferred from the
legacy notebooks.

## Required repository resolution order

1. Preserve `data/manifests/paper_40_images.csv` as the canonical author-confirmed
   manuscript evaluation subset.

2. Preserve `notebooks/legacy/` unchanged as historical evidence.

3. Keep the final manuscript implementation separate under `notebooks/final/`.

4. Add final implementation code only when it genuinely corresponds to the protocol
   reported in the manuscript.

5. Add final row-level outputs and table/figure source data only when they are genuine
   experimental records.

6. Record final checkpoint revisions, preprocessing settings, locality parameters,
   surrogate settings, split procedures, repeat counts, and aggregation procedures
   where those values can be verified.

7. Update traceability and audit documents when supporting evidence is added.

8. Do not relabel legacy exploratory outputs as final manuscript evidence merely because
   they resemble manuscript results.

9. Keep manuscript-transcribed tables labelled `MANUSCRIPT-TRANSCRIBED` unless they
   are independently regenerated from the verified final implementation and corresponding
   experiment records.

## Current conclusion

The repository is **AMBER** because it now provides substantially clearer documentation,
an author-confirmed 40-image evaluation manifest, aligned seven-author metadata,
separation of legacy and final implementation areas, manuscript-transcribed result
records, and explicit provenance categories.

The earlier 40-image subset-identifier gap is resolved.

The remaining AMBER status concerns reproducibility and provenance of the complete
final experimental pipeline and numerical/figure source records. These gaps should be
resolved by preserving or adding genuine final implementation and experimental evidence,
not by modifying legacy notebooks or inventing missing configuration values.
