# Final repository status

**Repository release status: AMBER.**

The ConceptSMILE repository is suitable as a transparent, limited research repository
under its existing rights statement. The AMBER status reflects remaining gaps in
end-to-end experimental reproducibility and result provenance. It does not indicate
that every manuscript result has been independently reproduced from the repository.

The repository distinguishes between:

- manuscript-reported methods and results;
- preserved historical notebook evidence;
- reconstructed reusable software utilities;
- manuscript-transcribed result tables; and
- material intended for the final manuscript implementation.

## Resolved repository-alignment items

Several issues identified during the original repository audit have now been resolved.

- The author-confirmed 40-image evaluation subset is documented in
  `data/manifests/paper_40_images.csv`.
- The manifest contains 10 image identifiers each from HRF, APTOS 2019, ODIR-5K,
  and IDRiD.
- `configs/paper.yaml` links to the evaluation manifest and identifies the current
  reviewed manuscript.
- `data/manifests/README.md` documents the evaluation subset in human-readable form.
- `docs/datasets.md` documents the 40-image evaluation subset.
- The root `README.md` links to the evaluation manifest and distinguishes historical
  notebooks from manuscript-aligned implementation material.
- `notebooks/legacy/` remains explicitly identified as historical evidence rather than
  the final manuscript implementation.
- `CITATION.cff` lists all seven manuscript authors.
- `pyproject.toml` lists all seven manuscript authors.
- The manuscript dataset citations are completed.
- The manuscript Code Availability statement contains the ConceptSMILE repository URL.
- The manuscript Author Contributions section is completed.
- Repository audit and reproducibility documentation has been updated to reflect the
  availability of the 40-image manifest.

The manuscript-reported numerical tables remain labelled
`MANUSCRIPT-TRANSCRIBED` where independent regeneration from final row-level outputs
has not yet been established.

## Remaining reproducibility and provenance gaps

The following issues remain unresolved and require genuine experimental records,
verified implementation details, or an independently documented rerun rather than
inferred or invented values:

- independent attribution-reference provenance;
- correspondence between the final MedSAM implementation and the common manuscript
  protocol;
- concept-specific VLM affected-region evidence;
- repeated concept-importance records supporting the consistency analysis;
- exact Table 4 locality, aggregation, and significance-calculation provenance;
- Table 6 variance/standard-deviation aggregation provenance;
- source verification for repeated values appearing across Tables 3 and 7;
- complete Figure 9 source data and final target-generation provenance;
- complete Figures 10–11 robustness source data;
- exact identity of the representative HRF robustness image;
- complete date/logo stability experiment records;
- complete VLM robustness execution records;
- exact final model/checkpoint revisions or hashes;
- final preprocessing details where not explicitly preserved;
- locality kernel widths and any operational normalisation;
- final XGBoost hyperparameters;
- train/test or validation split settings;
- repeat counts and aggregation rules; and
- a coherent final experimental environment record.

Unknown settings should remain explicitly unknown until genuine evidence is recovered.

See:

`docs/audits/final-scientific-audit.md`

and:

`MANUSCRIPT_CODE_TRACEABILITY.md`

for detailed evidence-level analysis.

## Current manuscript status

The earlier dataset-citation, code-availability, and author-contribution placeholders
have been resolved in the current manuscript.

Several manuscript-level editorial or metadata corrections remain separate from the
repository reproducibility issues:

- Mehran Hosseinalizadeh is marked with affiliation superscript `4`, but affiliation 4
  is not currently printed in the title-page affiliation list;
- `Vision language model provide` should be corrected to
  `Vision–language models provide`;
- the Section 5.2.6 heading `Attribution Fidelity` should be aligned with the
  surrogate-fidelity terminology used in the section; and
- `multiple segmentation models and vision–language model` should use the plural
  `vision–language models`.

These are manuscript editorial or metadata issues and should not be addressed by
altering experimental evidence in the repository.

## Validation already performed

The current reusable software package has been validated through GitHub Actions on
Python 3.10 and Python 3.11.

The latest completed CI validation recorded:

- package installation passed;
- Ruff checks passed;
- 33 unit tests passed;
- the synthetic smoke test passed;
- `configs/paper.yaml` validation passed; and
- the Python package build passed.

Earlier repository-audit validation also included:

- package import and entry-point checks;
- configuration/YAML/CFF parsing;
- Table 6 arithmetic auditing covering 48 displayed variance/SD pairs;
- Table 4 auditing covering 144 displayed values;
- cross-table exact-value matching;
- manuscript-table transcription checking;
- historical notebook preservation checks;
- Markdown target checking;
- current-tree credential-pattern scanning; and
- documentation build validation.

Full details and the distinction between the earlier audit and current CI validation
are recorded in:

`docs/audits/validation.md`

These checks establish software, documentation, transcription, and provenance
validation only. They are **not** equivalent to rerunning the complete retinal
experiments reported in the manuscript.

## Experimental execution status

No complete model-heavy four-dataset retinal experiment has been independently rerun
as part of the repository audit.

The preserved historical notebooks remain under `notebooks/legacy/` and should not be
modified simply to make their settings appear consistent with the final manuscript.

Final manuscript implementation material should remain separate from the historical
notebooks and should be clearly associated with:

- the 40-image evaluation manifest;
- the resolved experiment configuration;
- exact model/checkpoint information;
- runtime/environment information;
- row-level outputs; and
- table/figure generation inputs.

Any newly executed experiments should be explicitly labelled `RE-RUN` and should not
overwrite the historical `MANUSCRIPT-TRANSCRIBED` records.

## Data, models, rights, and security

The repository does not redistribute the four source retinal datasets or model weights.
Users must obtain the datasets from their respective providers.

Manuscript figures are retained for documentation and traceability where present.
Their inclusion does not establish independent redistribution rights for every
underlying retinal image or third-party graphical element.

The existing rights statement remains in place. A separate author decision is required
before the software is described as open source or broader reuse rights are granted.

Credential-pattern checking of the reviewed repository tree is not equivalent to a
complete Git-history security audit. Repository history should therefore be reviewed
separately before any future visibility change or public release.

## Repository history

The original repository audit used commit:

`83a10462036a7b8de7ce356cf617a98d67357131`

as its comparison baseline.

The live repository has subsequently been updated through explicit documentation,
manifest, metadata, software, validation, and traceability commits. The original
commit therefore remains a historical audit baseline rather than a description of the
current repository state.

## Current conclusion

ConceptSMILE remains **AMBER** because the repository is substantially better aligned
with the current manuscript and provides clearer provenance, while complete
end-to-end reproduction of the final experimental pipeline has not yet been
independently established.

The previous 40-image evaluation-subset gap is resolved.

The principal remaining scientific work concerns final implementation and result
provenance: preserving genuine final experiment code, exact configuration information,
row-level outputs, and the source data used to generate the reported tables and figures.

Missing evidence should be recovered or regenerated through a clearly documented rerun.
Historical notebooks or manuscript-transcribed values should not be altered merely to
create the appearance of reproducibility.
