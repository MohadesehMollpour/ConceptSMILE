#!/usr/bin/env python3
"""Exercise deterministic ConceptSMILE components without datasets or checkpoints."""

from __future__ import annotations

import numpy as np

from conceptsmile.locality.distances import cosine_distance, exponential_kernel
from conceptsmile.metrics.fidelity import evaluate_fidelity
from conceptsmile.perturbation.superpixels import (
    apply_superpixel_perturbation,
    sample_binary_perturbations,
)


def main() -> int:
    image = np.full((4, 4, 3), 255, dtype=np.uint8)
    segments = np.repeat(np.arange(4).reshape(2, 2), 2, axis=0)
    segments = np.repeat(segments, 2, axis=1)
    vectors = sample_binary_perturbations(4, 6, seed=42)
    perturbed = apply_superpixel_perturbation(image, segments, vectors[0])

    distances = cosine_distance(np.array([1.0, 0.0]), np.array([[1.0, 0.0], [0.0, 1.0]]))
    weights, _ = exponential_kernel(distances, sigma=0.25)
    metrics = evaluate_fidelity(
        np.array([0.0, 1.0]), np.array([0.0, 0.9]), np.array([1.0, 0.5])
    )

    print("vectors", vectors.shape)
    print("masked_pixels", int(np.count_nonzero(perturbed == 0)))
    print("weights", weights.tolist())
    print("fidelity", metrics.to_dict())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

