# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Reconstructed superpixel and masking utilities derived from preserved notebooks."""

from __future__ import annotations

from collections.abc import Sequence

import numpy as np
from skimage.color import rgb2gray
from skimage.segmentation import slic
from skimage.util import img_as_float


def generate_superpixels(
    image: np.ndarray,
    *,
    n_segments: int = 7,
    compactness: float = 18.0,
    sigma: float = 1.0,
    mask_retina: bool = True,
    retina_threshold: float = 0.05,
) -> np.ndarray:
    """Create SLIC labels using the VLM notebook's recorded defaults.

    ``n_segments`` is a target rather than a guarantee; SLIC may return fewer
    connected regions. Pixels outside the optional retinal mask can be labelled
    ``-1`` and are not treated as perturbable regions.
    """
    array = np.asarray(image)
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("image must have shape (height, width, 3)")
    if n_segments < 1:
        raise ValueError("n_segments must be positive")

    mask = rgb2gray(array) > retina_threshold if mask_retina else None
    if mask is not None and not np.any(mask):
        mask = np.ones(array.shape[:2], dtype=bool)

    return slic(
        img_as_float(array),
        n_segments=n_segments,
        compactness=compactness,
        sigma=sigma,
        start_label=0,
        enforce_connectivity=True,
        mask=mask,
    )


def segment_labels(segments: np.ndarray) -> np.ndarray:
    """Return sorted non-background segment labels."""
    labels = np.unique(np.asarray(segments))
    return labels[labels >= 0]


def build_superpixel_masks(segments: np.ndarray) -> np.ndarray:
    """Convert an integer label map to ``(regions, height, width)`` masks."""
    labels = segment_labels(segments)
    return np.stack([segments == label for label in labels], axis=0).astype(bool)


def sample_binary_perturbations(
    n_regions: int,
    n_perturbations: int = 50,
    *,
    seed: int = 42,
    unique: bool = True,
    exclude_all_masked: bool = True,
) -> np.ndarray:
    """Sample binary keep/remove vectors.

    The VLM notebook used NumPy's ``default_rng`` with unique vectors and
    changed an all-zero draw by retaining one randomly selected region. The
    legacy MedSAM notebook did not enforce uniqueness; set ``unique=False`` to
    retain that behaviour.
    """
    if n_regions < 1 or n_perturbations < 1:
        raise ValueError("n_regions and n_perturbations must be positive")

    available = (2**n_regions) - int(exclude_all_masked)
    if unique and n_perturbations > available:
        raise ValueError(
            f"cannot draw {n_perturbations} unique vectors from {available} allowed states"
        )

    rng = np.random.default_rng(seed)
    vectors: list[np.ndarray] = []
    seen: set[tuple[int, ...]] = set()

    while len(vectors) < n_perturbations:
        keep = rng.integers(0, 2, size=n_regions, dtype=np.int64)
        if exclude_all_masked and int(keep.sum()) == 0:
            keep[int(rng.integers(0, n_regions))] = 1

        key = tuple(int(value) for value in keep)
        if unique and key in seen:
            continue
        seen.add(key)
        vectors.append(keep)

    return np.stack(vectors, axis=0).astype(int)


def apply_superpixel_perturbation(
    image: np.ndarray,
    segments: np.ndarray,
    keep_vector: Sequence[int] | np.ndarray,
    *,
    fill_value: int | float = 0,
) -> np.ndarray:
    """Set removed superpixels to a constant value (black in the paper)."""
    array = np.asarray(image)
    label_map = np.asarray(segments)
    labels = segment_labels(label_map)
    keep = np.asarray(keep_vector).reshape(-1)

    if array.shape[:2] != label_map.shape:
        raise ValueError("image and segments must have matching spatial dimensions")
    if len(keep) != len(labels):
        raise ValueError(f"keep_vector has {len(keep)} values for {len(labels)} regions")
    if not np.isin(keep, [0, 1]).all():
        raise ValueError("keep_vector must contain only 0 and 1")

    perturbed = array.copy()
    for column, label in enumerate(labels):
        if keep[column] == 0:
            perturbed[label_map == label] = fill_value
    return perturbed

