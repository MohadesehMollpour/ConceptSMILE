# Final repository status

**AMBER: suitable as a transparent, limited public research repository under the existing rights statement.** This is not approval of the manuscript's disputed numerical claims, independent attribution validation or full reproduction. An author decision is still needed on a reusable software licence; no open-source licence has been imposed.

Fixed: misleading metric interpretations; contradictory live documentation; missing table arithmetic/provenance registers; degenerate input/weight validation; unverified imagery in the public package. Notebook source cells and plain-text numerical outputs remain unchanged in explicitly sanitised derivatives, with original/release hashes. Manuscript values are unchanged and labelled MANUSCRIPT-TRANSCRIBED.

Unresolved: independent attribution references; common MedSAM/paper protocol; concept-specific VLM affected evidence; importance-score consistency; Table4 locality/p-values; Table6 scaling/aggregation; Table3/7 repeated pairs; Figure9 targets; Figure10–11 source data/HRF identity; date/logo experiments; exact 40-image manifest; checkpoint hashes and coherent historical environment. See docs/audits/final-scientific-audit.md. Recover original evidence before replacing values.

**Manuscript claims need correction or additional evidence.** Attribution, faithfulness, consistency and figure/table interpretations require review. Dataset citation, code-link and author-contribution placeholders also remain in the supplied PDF. The PDF was not modified.

Validation actually run: 28 unit tests passed; all 22 discovered package modules imported; package entry point and synthetic smoke test passed; configuration/YAML/CFF parsing passed; Ruff passed. Arithmetic audit covers 48 Table6 pairs (1 compatible with printed rounding, 43 possibly coarser rounding, 4 inconsistent under the stated single-distribution tests) and 144 Table4 values. Table transcriptions compared byte-for-byte; sanitisation preservation assertions passed. Final Markdown links and current-tree credential-pattern checks passed. Documentation build checked; full details in docs/audits/validation.md.

No model-heavy retinal experiment was rerun. No dataset, model weights, image assets, NHS logo, secrets, caches, virtual environment or .git directory is included. Limited credential scans are not a full Git-history security audit.

Prepared locally from submission-ready commit 83a10462036a7b8de7ce356cf617a98d67357131, verified against the live branch. No push, merge, release, visibility change or Git-history rewrite was performed. Publishing an existing repository's history requires separate review; this assessment covers the ZIP contents only.
