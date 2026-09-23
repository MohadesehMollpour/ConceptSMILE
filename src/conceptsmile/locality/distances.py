# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Embedding distances and exponential locality weights."""

from __future__ import annotations

import numpy as np
from scipy.stats import wasserstein_distance


def cosine_distance(reference: np.ndarray, samples: np.ndarray) -> np.ndarray:
    """Return cosine distance from one reference vector to one or more samples."""
    reference_array = np.asarray(reference, dtype=np.float32).reshape(-1)
    sample_array = np.asarray(samples, dtype=np.float32)
    was_vector = sample_array.ndim == 1
    sample_array = np.atleast_2d(sample_array)
    if sample_array.shape[1] != reference_array.shape[0]:
        raise ValueError("reference and samples must have the same embedding dimension")

    denominator = (
        np.linalg.norm(sample_array, axis=1) * np.linalg.norm(reference_array) + 1e-12
    )
    similarity = (sample_array @ reference_array) / denominator
    distance = np.clip(1.0 - similarity, 0.0, 2.0)
    return distance[0] if was_vector else distance


def exponential_kernel(
    distances: np.ndarray,
    *,
    sigma: float | None = None,
    half_factor: bool = False,
    minimum_weight: float | None = None,
) -> tuple[np.ndarray, float]:
    """Convert distances to locality weights.

    The notebooks used ``exp(-d²/sigma²)`` for cosine distance and
    ``exp(-d²/(2*sigma²))`` for normalised Wasserstein distance.
    """
    values = np.asarray(distances, dtype=float)
    if not values.size or not np.isfinite(values).all() or (values < 0).any():
        raise ValueError("distances must be finite, nonnegative and nonempty")
    if minimum_weight is not None and not 0 <= minimum_weight <= 1:
        raise ValueError("minimum_weight must be between zero and one")
    if sigma is None:
        positive = values[values > 0]
        sigma = float(np.median(positive)) if positive.size else 0.25
    if not np.isfinite(sigma) or sigma <= 0:
        raise ValueError("sigma must be finite and greater than zero")

    denominator = (2.0 if half_factor else 1.0) * sigma**2
    weights = np.exp(-(values**2) / denominator)
    if minimum_weight is not None:
        weights = np.clip(weights, minimum_weight, None)
    return weights.astype(float), float(sigma)


def wasserstein_embedding_distance(reference: np.ndarray, samples: np.ndarray) -> np.ndarray:
    """Apply SciPy's one-dimensional Wasserstein distance to embedding values."""
    reference_array = np.asarray(reference, dtype=float).reshape(-1)
    sample_array = np.asarray(samples, dtype=float)
    was_vector = sample_array.ndim == 1
    sample_array = np.atleast_2d(sample_array)
    if sample_array.shape[1] != reference_array.shape[0]:
        raise ValueError("reference and samples must have the same embedding dimension")
    distances = np.asarray(
        [wasserstein_distance(reference_array, sample) for sample in sample_array], dtype=float
    )
    return distances[0] if was_vector else distances


def wasserstein_locality_weights(
    distances: np.ndarray,
    *,
    sigma: float = 0.75,
) -> tuple[np.ndarray, np.ndarray]:
    """Min-max normalise Wasserstein distances and apply the notebook kernel."""
    values = np.asarray(distances, dtype=float)
    if not values.size or not np.isfinite(values).all() or (values < 0).any():
        raise ValueError("distances must be finite, nonnegative and nonempty")
    minimum = float(np.min(values))
    maximum = float(np.max(values))
    normalised = (
        (values - minimum) / (maximum - minimum)
        if maximum > minimum
        else np.zeros_like(values)
    )
    weights, _ = exponential_kernel(normalised, sigma=sigma, half_factor=True)
    return normalised.astype(float), weights

