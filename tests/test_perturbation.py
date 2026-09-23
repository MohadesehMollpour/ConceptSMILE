import numpy as np

from conceptsmile.perturbation.superpixels import (
    apply_superpixel_perturbation,
    build_superpixel_masks,
    sample_binary_perturbations,
)


def test_unique_perturbations_are_deterministic_and_not_all_zero():
    first = sample_binary_perturbations(7, 50, seed=42)
    second = sample_binary_perturbations(7, 50, seed=42)

    assert np.array_equal(first, second)
    assert first.shape == (50, 7)
    assert len({tuple(row) for row in first}) == 50
    assert np.all(first.sum(axis=1) > 0)


def test_apply_perturbation_masks_selected_region():
    image = np.full((2, 4, 3), 255, dtype=np.uint8)
    segments = np.array([[0, 0, 1, 1], [0, 0, 1, 1]])
    output = apply_superpixel_perturbation(image, segments, [1, 0])

    assert np.all(output[:, :2] == 255)
    assert np.all(output[:, 2:] == 0)
    assert build_superpixel_masks(segments).shape == (2, 2, 4)

