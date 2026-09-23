# Contributing

Contributions are welcome after the maintainers confirm the public licence.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

## Local checks

```bash
ruff check .
pytest
python -m build
mkdocs build --strict
```

## Scientific changes

- Link each changed algorithm or parameter to the originating manuscript section, notebook cell, or reviewed issue.
- Do not silently change seeds, thresholds, prompts, model revisions, dataset membership, or metrics.
- Add or update a configuration and test for reusable behaviour.
- Include the dataset source, licence, selection criteria, and checksum for new manifests.
- Keep notebooks as demonstrations or provenance records; move stable reusable logic into `src/conceptsmile/`.
- Report any result that changes and explain why; do not overwrite historical artefacts without provenance.

Never commit datasets, credentials, patient information, private metadata, or large model checkpoints.

