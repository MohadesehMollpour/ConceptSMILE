# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Small MedSAM utilities extracted without changing the notebook's scoring logic."""

from __future__ import annotations

import numpy as np


def mask_confidence(soft_mask: np.ndarray, threshold: float = 0.5) -> float:
    """Return mean probability inside the thresholded mask."""
    soft = np.asarray(soft_mask, dtype=float)
    binary = soft > threshold
    if not np.any(binary):
        return 0.0
    return float(soft[binary].mean())


def mask_bbox(mask: np.ndarray) -> tuple[int, int, int, int] | None:
    """Return ``(x0, y0, x1, y1)`` for a non-empty binary mask."""
    y_coordinates, x_coordinates = np.where(np.asarray(mask, dtype=bool))
    if x_coordinates.size == 0:
        return None
    return (
        int(x_coordinates.min()),
        int(y_coordinates.min()),
        int(x_coordinates.max()),
        int(y_coordinates.max()),
    )


def pool_medsam_embedding(embedding: object) -> np.ndarray:
    """Global-average-pool a MedSAM image embedding as in the legacy notebook."""
    if hasattr(embedding, "detach"):
        embedding = embedding.detach().cpu().numpy()  # type: ignore[union-attr]
    array = np.asarray(embedding, dtype=np.float32)

    if array.ndim == 4:
        pooled = array.mean(axis=(0, 2, 3))
    elif array.ndim == 3:
        pooled = array.mean(axis=(1, 2))
    elif array.ndim == 2:
        pooled = array.mean(axis=0)
    elif array.ndim == 1:
        pooled = array
    else:
        raise ValueError(f"unexpected MedSAM embedding shape: {array.shape}")
    return np.asarray(pooled, dtype=np.float32)

