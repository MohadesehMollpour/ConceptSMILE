# Manuscript-transcribed tables

Provenance: `MANUSCRIPT-TRANSCRIBED`.

Source manuscript:

- `Moha___ConceptSMILE (16).pdf`
- 49 pages
- SHA-256: `9178fc53e22cc259142915264e9d52c8d7769c6aa8ec820b10057d743d90470c`

Tables 2–7 were transcribed from the current reviewed manuscript and checked against
the rendered pages.

Current table locations are:

- Table 2: p.24
- Table 3: p.26
- Table 4: p.27
- Table 5: p.29
- Table 6: p.31
- Table 7: p.34

Values are preserved at the precision displayed in the manuscript, including values
flagged elsewhere for provenance or arithmetic review.

These files are **not original raw experimental outputs** and are **not computational
reproductions** of the reported experiments.

Table 6 retains the manuscript's printed scale factors:

- variance ×10^-4
- standard deviation ×10^-3

The repository does not silently alter displayed variance/standard-deviation pairs.
Any interpretation of those values must use the documented aggregation procedure and
source repeated-run records when available.

For Table 4, a displayed value such as `p = 0.0000` is retained as the manuscript's
rounded presentation and should not be interpreted as proof that the underlying
probability is exactly zero.

Table 5 retains both MedSAM and VLM pathway values as presented in the manuscript.

Aggregation units, per-statistic sample sizes, and underlying row-level experimental
inputs remain unresolved where they have not been independently recovered.

No point-level coordinates were reconstructed or invented from Figures 9–11.

Figure source-data requirements and remaining provenance gaps are documented in:

- `MANUSCRIPT_CODE_TRACEABILITY.md`
- `docs/audits/manuscript-review.md`
- `docs/audits/final-scientific-audit.md`

A script that reads, checks, or prints these manuscript-transcribed values must not be
described as reproducing the underlying retinal experiments.

These tables should remain labelled `MANUSCRIPT-TRANSCRIBED` unless they are
independently regenerated from a verified final implementation and corresponding
experimental records.
