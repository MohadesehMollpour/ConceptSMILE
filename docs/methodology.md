# Methods and evidence boundaries

See [scientific provenance](scientific_provenance.md), [manuscript audit](audits/manuscript-review.md) and the repository-root `MANUSCRIPT_CODE_TRACEABILITY.md`.

The manuscript proposes binary SLIC perturbations, concept-response shifts, exponential locality and weighted XGBoost regression. Preserved implementations differ: MedSAM uses target12/nonunique draws and pooled MedSAM embeddings; VLM uses target7/unique draws and DINOv2 CLS. Black masks and all-zero repair appear in both. Legacy configs record these differences. Wasserstein operates on empirical distributions of embedding components, min-max normalises distances, and uses a kernel with factor2 in the denominator; it is not spatial optimal transport.

Historical MedSAM reference metrics mean model-mask-reference agreement. Historical VLM attribution numbers mean a self-referential diagnostic corrupted by positional alignment, not independent clinical accuracy. VLM correlation uses global removal fraction. Legacy repeated-run statistics are R² dispersion. Generic metrics in src support caller-defined inputs but do not reproduce missing paper experiments.

Figure9 cannot be assigned one verified target: V13/15 uses confidence and an in-sample fit; M26/29 uses held-out shifts, and V21 uses shifts. The paper's complete plot source is absent. No unified target is invented.
