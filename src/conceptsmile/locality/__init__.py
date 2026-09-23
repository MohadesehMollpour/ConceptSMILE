# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Distance functions and locality kernels."""

from .distances import (
    cosine_distance,
    exponential_kernel,
    wasserstein_embedding_distance,
    wasserstein_locality_weights,
)

__all__ = [
    "cosine_distance",
    "exponential_kernel",
    "wasserstein_embedding_distance",
    "wasserstein_locality_weights",
]

