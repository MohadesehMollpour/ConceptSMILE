# Manuscript-to-evidence audit

Reviewed: `Moha___ConceptSMILE (1)(2).pdf`, 46 pages, SHA-256 c4a9c68fe7ae240530a6db9a3509d4116d94cd59976fec259b6ec71d2d87d992. Printed and PDF page numbers agree. Scientific methods, all numerical tables and quantitative figures were checked using text extraction and rendered pages. No manuscript values were altered. Citation correctness across the entire external bibliography has not been independently audited.

## Verified manuscript statements versus historical execution

| Location | Verified manuscript statement | Preserved evidence / assessment |
| --- | --- | --- |
| Section 4.1, pp.13–14 | MedSAM and semantic VLM concept pathways | Both single-image notebooks present; not complete same-image four-dataset pairing |
| Section 4.2, Eqs.3–6, pp.14–15 | Binary superpixel masks and original-minus-perturbed response shift | Broadly supported by preserved code; unique sampling differs by pathway |
| Table 1, p.21 | 40 images, ten per dataset; 50 unique masks; target SLIC 7; DINOv2 CLS | MedSAM uses target 12, six realised segments, non-unique draws, pooled MedSAM embeddings; historical 40-image IDs absent |
| Section 4.3, Eq.9, p.16 | exp(−d²/sigma²) | Wasserstein notebook code min-max normalises and uses exp(−d_norm²/(2×0.75²)); factor 2 can be absorbed into width, but operational normalisation/width must be documented |
| Section 4.3, Eq.10, p.16 | Weighted XGBoost shift regression | Repeated single-image code exists; settings/held-out split details not given in Table 1 |
| Section 4.4, Eq.11, p.17; Table 3, p.25 | Clinically relevant attribution references | VLM labels circular and row-misaligned; MedSAM references are model-derived masks, not independent annotation |
| Section 4.4, Eqs.12–15, p.18 | WMSE, WMAE, weighted R² | Reusable formula helpers agree for valid nondegenerate inputs; no proof of table reproduction |
| Section 4.4, Eq.16, p.19; Table 4, p.27 | Concept-relevant strength versus absolute shift | VLM uses global removed fraction; M uses predicted-mask fraction |
| Section 4.4, Eq.17, p.19; Table 5, p.29 | Date/logo Jaccard stability | No experiment or original explanation sets supplied; generic Jaccard helper only |
| Section 4.4, Eqs.18–19, p.19; Table 6, p.31 | Sample variance and SD of repeated concept importance | Preserved code reports repeated split R² dispersion; no importance-score provenance |
| Section 5.3, p.33; Figs.10–11, p.35 | Representative HRF image; contrast .6–1.4; occlusion 0–3% | Available M notebook loads ODIR image1.png; V experiment absent; do not relabel the image HRF |
| Title page, p.1 | Six named authors | Matches existing CFF author list and package metadata |
| Section 6, pp.37–38 | Proof of concept, no causal proof, no clinician/prospective testing | Appropriate limitations; they do not resolve unsupported numerical provenance |

## Further manuscript issues requiring original results

1. **Table 4 locality dependence is unexplained.** M42 and V25 use ordinary `pearsonr` on the same strength/shift inputs, without locality weights. Merely switching cosine/Wasserstein surrogate weights cannot change those correlations. Table 4 reports different correlations in both columns. Recover the actual calculation, sample selection and aggregation before accepting either column. Do not invent a weighted Pearson implementation to fit the table.
2. **Table 4 significance reporting needs review.** M42 computes a mean of node p-values; that is not a combined significance test. The manuscript does not identify the independent sample unit or how table SD and p-values are aggregated. Section 5.2.3 p.26 says IDRiD MedSAM relationships did not reach p<.05, but Table 4 reports Wasserstein optic-disc p=.0378. If the text is about cosine only, say so. The VLM IDRiD vessel p is printed .0000 in the table versus .0001 in prose; report rounding accurately after checking source values.
3. **Table 6 scale/aggregation concern.** APTOS MedSAM lesion shows variance .0100×10^-4=10^-6 but SD .0010×10^-3=10^-6 in both columns. For a single repeated-score distribution Eq.19 requires SD=sqrt(variance)=10^-3. ODIR MedSAM optic disc has the same displayed variance but SD .0110×10^-3 or .0120×10^-3. These pairs do not satisfy Eq.19 as a single summary distribution. Separate averaging of variance and SD could change that relation, but would require an explicit aggregation rule and source records. No values were automatically corrected.
4. **Table 3/Table 7 repeated pairs need source checking.** For example Table 7 VLM APTOS cosine R²/Rw² .5328/.5414, .5511/.5512 and .7362/.7343 exactly repeat Table 3 VLM HRF cosine ACC/F1. Table 7 VLM APTOS Wasserstein .4762/.4754, .5016/.5453 and .6316/.6562 repeat Table 3 VLM APTOS cosine ACC/F1. This is a possible copying/mapping problem, not proof of fabrication. Recover calculation outputs and table assembly source.
5. **Figure 9 target ambiguity.** Page 32 labels axes actual/predicted confidence, while Eqs.6/10 and fidelity text define the regression target as confidence shift. M and V exploratory plotting cells differ in target treatment. Recover figure data and state whether panels show scores, shifts, or confidence reconstructed from shift. Some M plotted values are negative, reinforcing the need to check the axis semantics.
6. **Figure 11 is not established as M44 output.** Manuscript Figure 11 includes an optic-disc series. The saved corrected M44 summary lacks optic-disc rows and its plotting code displays not-estimable panels when unavailable. M43 is another retained version; neither should be selected solely because it visually resembles a paper plot. Establish source cell/version, dataset and row-level inputs.
7. **Implementation details missing from manuscript.** Page 20 says Table 1 summarises seeds, but no seed row is present. Preprocessing, kernel widths/normalisation, XGBoost parameters, train/test split and repeat counts, checkpoint revisions and exact subset identifiers remain undocumented at paper level. Legacy values are not automatically paper values. Clarify whether 2,000 perturbed samples means images shared between pathways or inference calls per pathway.

## Manuscript completion items

- Table 1 p.21: unresolved APTOS and ODIR citations `[?]`.
- Code availability p.40: `[repository link]` placeholder remains. Working branch is private; do not promise current public access.
- Author contributions p.41: four `[add confirmed contributions]` placeholders remain. Obtain genuine contributions; do not infer them from author order.
- Confirm whether report aggregation is over images, nodes, concepts or repeats and identify uncertainty units. Ten images per dataset do not make every perturbation an independent clinical sample.

## Required resolution order

Recover original row-level outputs, image IDs and figure/table assembly sources first. Determine which discrepancies are manuscript-description errors versus implementation errors. Then correct manuscript claims or run explicitly new evaluations with independent labels and documented protocols. Store new results separately as RE-RUN. The present transcribed tables remain unchanged as a record of the reviewed version. Manuscript claims still require review. The separately scoped final repository release is AMBER because it no longer claims to reproduce or validate these results.
