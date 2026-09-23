import numpy as np

from conceptsmile.metrics.attribution import evaluate_attribution
from conceptsmile.metrics.consistency import consistency_statistics
from conceptsmile.metrics.faithfulness import pearson_faithfulness
from conceptsmile.metrics.fidelity import evaluate_fidelity, weighted_r2
from conceptsmile.metrics.stability import jaccard_index


def test_perfect_fidelity():
    y = np.array([0.0, 0.5, 1.0])
    metrics = evaluate_fidelity(y, y, np.array([1.0, 0.5, 0.25]))

    assert metrics.mse == 0.0
    assert metrics.wmse == 0.0
    assert metrics.r2 == 1.0
    assert metrics.weighted_r2 == 1.0
    assert weighted_r2(y, y, np.ones_like(y)) == 1.0


def test_faithfulness_and_consistency():
    result = pearson_faithfulness(
        np.array([0.0, 0.5, 1.0]), np.array([0.0, -0.5, 1.0])
    )
    variance, standard_deviation = consistency_statistics(np.array([1.0, 2.0, 3.0]))

    assert np.isclose(result.correlation, 1.0)
    assert result.status == "ok"
    assert np.isclose(variance, 1.0)
    assert np.isclose(standard_deviation, 1.0)


def test_attribution_and_jaccard():
    metrics = evaluate_attribution(
        np.array([0, 0, 1, 1]), np.array([0.1, 0.2, 0.8, 0.9]), threshold=0.5
    )

    assert metrics.accuracy == 1.0
    assert metrics.f1 == 1.0
    assert metrics.auroc == 1.0
    assert jaccard_index({"lesion", "vessel"}, {"vessel", "optic_disc"}) == 1 / 3

