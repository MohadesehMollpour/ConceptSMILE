import numpy as np
import pytest

from conceptsmile.metrics.attribution import evaluate_attribution
from conceptsmile.metrics.fidelity import weighted_mae, weighted_mse, weighted_r2
from conceptsmile.perturbation.superpixels import (
    apply_superpixel_perturbation,
    sample_binary_perturbations,
)


def test_weighted_metrics_hand_calculated():
    y, predicted, w = np.array([0., 2.]), np.array([1., 1.]), np.array([1., 3.])
    assert weighted_mse(y, predicted, w) == 1.
    assert weighted_mae(y, predicted, w) == 1.
    assert np.isclose(weighted_r2(y, predicted, w), -1 / 3)


@pytest.mark.parametrize('weights', [[0, 0], [-1, 2], [1, np.nan]])
def test_invalid_weights_rejected(weights):
    with pytest.raises(ValueError):
        weighted_mse([0, 1], [0, 1], weights)


def test_empty_metric_rejected():
    with pytest.raises(ValueError):
        weighted_mae([], [], [])


def test_fractional_labels_not_silently_truncated():
    with pytest.raises(ValueError):
        evaluate_attribution([0, 1.5], [0.1, 0.9], threshold=0.5)
    with pytest.raises(ValueError):
        apply_superpixel_perturbation(np.ones((1, 2, 3)), np.array([[0, 1]]), [1, 0.5])


def test_adaptive_threshold_disclosed():
    result = evaluate_attribution([0, 0, 1, 1], [0.1, 0.2, 0.8, 0.9])
    assert result.status == 'exploratory_same_sample_threshold'


def test_impossible_unique_request_fails():
    with pytest.raises(ValueError):
        sample_binary_perturbations(2, 4, unique=True, exclude_all_masked=True)


def test_background_is_preserved():
    image = np.ones((1, 3, 3))
    labels = np.array([[-1, 0, 1]])
    result = apply_superpixel_perturbation(image, labels, [0, 1])
    assert np.array_equal(result[:, 0], image[:, 0])
    assert np.all(result[:, 1] == 0)
    assert np.array_equal(result[:, 2], image[:, 2])


@pytest.mark.parametrize('labels,scores,weights', [([], [], []), ([0], [np.nan], [1]),
                                                 ([1], [0.5], [-1])])
def test_attribution_degenerate_inputs_validate_first(labels, scores, weights):
    with pytest.raises(ValueError):
        evaluate_attribution(labels, scores, sample_weights=weights)


def test_single_observation_negative_weight_rejected():
    with pytest.raises(ValueError):
        weighted_r2([1], [1], [-1])


@pytest.mark.parametrize('distances', [[], [-1], [np.nan], [np.inf]])
def test_invalid_locality_distances_rejected(distances):
    from conceptsmile.locality.distances import exponential_kernel, wasserstein_locality_weights
    with pytest.raises(ValueError):
        exponential_kernel(distances)
    with pytest.raises(ValueError):
        wasserstein_locality_weights(distances)


def test_kernel_floor_cannot_create_invalid_weights():
    from conceptsmile.locality.distances import exponential_kernel
    with pytest.raises(ValueError):
        exponential_kernel([0, 1], minimum_weight=2)
