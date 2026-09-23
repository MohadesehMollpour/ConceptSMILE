# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Superpixel generation and controlled image perturbations."""

from .superpixels import (
    apply_superpixel_perturbation,
    build_superpixel_masks,
    generate_superpixels,
    sample_binary_perturbations,
)

__all__ = [
    "apply_superpixel_perturbation",
    "build_superpixel_masks",
    "generate_superpixels",
    "sample_binary_perturbations",
]

