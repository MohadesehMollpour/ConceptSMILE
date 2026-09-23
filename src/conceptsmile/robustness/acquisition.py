# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Controlled contrast and simulated occlusion utilities from the notebook."""

from __future__ import annotations

import numpy as np


def retinal_fov_mask(image: np.ndarray, threshold: float = 10.0) -> np.ndarray:
    """Estimate the non-black retinal field of view."""
    array = np.asarray(image)
    grey = array.astype(np.float32).mean(axis=2)
    mask = grey > threshold
    if int(mask.sum()) < 0.05 * mask.size:
        return np.ones(grey.shape, dtype=bool)
    return mask


def modify_retinal_contrast(image: np.ndarray, contrast_factor: float) -> np.ndarray:
    """Apply mean-preserving contrast modification inside the retinal field."""
    if contrast_factor <= 0:
        raise ValueError("contrast_factor must be greater than zero")
    array = np.asarray(image, dtype=np.uint8)
    image_float = array.astype(np.float32)
    mask = retinal_fov_mask(array)
    mean_rgb = image_float[mask].mean(axis=0)
    modified = image_float.copy()
    modified[mask] = mean_rgb + contrast_factor * (image_float[mask] - mean_rgb)
    return np.clip(modified, 0, 255).astype(np.uint8)


def add_simulated_occlusion(
    image: np.ndarray,
    occlusion_percentage: float,
    *,
    x_ratio: float = 0.5,
    darkness: float = 1.0,
) -> np.ndarray:
    """Add the notebook's vertical simulated acquisition occlusion."""
    if not 0 <= occlusion_percentage <= 100:
        raise ValueError("occlusion_percentage must be between 0 and 100")
    if not 0 <= x_ratio <= 1 or not 0 <= darkness <= 1:
        raise ValueError("x_ratio and darkness must lie in [0, 1]")
    array = np.asarray(image, dtype=np.uint8)
    if occlusion_percentage == 0:
        return array.copy()

    mask = retinal_fov_mask(array)
    _, x_coordinates = np.where(mask)
    x_minimum, x_maximum = int(x_coordinates.min()), int(x_coordinates.max())
    retinal_width = x_maximum - x_minimum + 1
    line_width = max(2, int(round(retinal_width * occlusion_percentage / 100.0)))
    line_centre = int(round(x_minimum + x_ratio * (retinal_width - 1)))
    line_start = max(0, line_centre - line_width // 2)
    line_end = min(array.shape[1], line_start + line_width)

    modified = array.astype(np.float32).copy()
    local_mask = mask[:, line_start:line_end]
    local_region = modified[:, line_start:line_end]
    modified[:, line_start:line_end] = np.where(
        local_mask[..., None], local_region * (1.0 - darkness), local_region
    )
    return np.clip(modified, 0, 255).astype(np.uint8)

