import numpy as np

from conceptsmile.locality.distances import (
    cosine_distance,
    exponential_kernel,
    wasserstein_embedding_distance,
    wasserstein_locality_weights,
)


def test_cosine_distance_and_kernel_order():
    reference = np.array([1.0, 0.0])
    samples = np.array([[1.0, 0.0], [0.0, 1.0]])
    distances = cosine_distance(reference, samples)
    weights, sigma = exponential_kernel(distances, sigma=0.25)

    assert np.allclose(distances, [0.0, 1.0])
    assert sigma == 0.25
    assert weights[0] > weights[1]


def test_wasserstein_weights_are_bounded():
    distances = wasserstein_embedding_distance(
        np.array([0.0, 1.0]), np.array([[0.0, 1.0], [2.0, 3.0]])
    )
    normalised, weights = wasserstein_locality_weights(distances)

    assert np.allclose(normalised, [0.0, 1.0])
    assert np.all((weights > 0) & (weights <= 1))

