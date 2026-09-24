import numpy as np

from conceptsmile.metrics.attribution import evaluate_attribution
from conceptsmile.metrics.consistency import (
    consistency_statistics,
    evaluate_consistency,
)
from conceptsmile.metrics.faithfulness import evaluate_faithfulness
from conceptsmile.metrics.fidelity import evaluate_fidelity
from conceptsmile.metrics.stability import (
    evaluate_stability,
    jaccard_index,
)


def test_perfect_fidelity():
    y = np.array([0.0, 0.5, 1.0])
    weights = np.array([1.0, 0.5, 0.25])

    metrics = evaluate_fidelity(
        y_true=y,
        y_pred=y,
        weights=weights,
    )

    assert metrics.mse == 0.0
    assert metrics.mae == 0.0
    assert metrics.wmse == 0.0
    assert metrics.wmae == 0.0
    assert metrics.r2 == 1.0
    assert metrics.weighted_r2 == 1.0
    assert metrics.n == 3


def test_faithfulness():
    result = evaluate_faithfulness(
        perturbation_strength=np.array(
            [0.0, 0.5, 1.0]
        ),
        response_shift=np.array(
            [0.0, -0.5, 1.0]
        ),
    )

    assert np.isclose(
        result.correlation,
        1.0,
    )
    assert result.status == "ok"
    assert result.n == 3


def test_consistency():
    scores = np.array(
        [1.0, 2.0, 3.0]
    )

    result = evaluate_consistency(scores)

    assert np.isclose(
        result.mean_importance,
        2.0,
    )
    assert np.isclose(
        result.variance,
        1.0,
    )
    assert np.isclose(
        result.standard_deviation,
        1.0,
    )
    assert result.n_runs == 3

    variance, standard_deviation = (
        consistency_statistics(scores)
    )

    assert np.isclose(
        variance,
        1.0,
    )
    assert np.isclose(
        standard_deviation,
        1.0,
    )


def test_attribution():
    metrics = evaluate_attribution(
        reference_labels=np.array(
            [0, 0, 1, 1]
        ),
        attribution_scores=np.array(
            [0.1, 0.2, 0.8, 0.9]
        ),
        threshold=0.5,
    )

    assert metrics.accuracy == 1.0
    assert metrics.f1 == 1.0
    assert metrics.auroc == 1.0
    assert metrics.threshold == 0.5
    assert metrics.n == 4


def test_stability():
    original = {
        "lesion",
        "vessel",
    }

    modified = {
        "vessel",
        "optic_disc",
    }

    result = evaluate_stability(
        original,
        modified,
    )

    assert result.jaccard == 1 / 3
    assert result.intersection_size == 1
    assert result.union_size == 3

    assert (
        jaccard_index(
            original,
            modified,
        )
        == 1 / 3
    )
