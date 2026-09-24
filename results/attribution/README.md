"""ConceptSMILE attribution-accuracy metrics.

Paper:
    Eq. (11)
    Metrics: Attribution Accuracy, F1, AUROC

Reference labels and threshold must be supplied by the experiment.
"""

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score


@dataclass(frozen=True)
class AttributionResult:
    accuracy: float
    f1: float
    auroc: float
    threshold: float


def evaluate_attribution(
    reference_labels,
    attribution_scores,
    threshold: float,
) -> AttributionResult:
    labels = np.asarray(reference_labels, dtype=int).reshape(-1)
    scores = np.asarray(attribution_scores, dtype=float).reshape(-1)

    if labels.size == 0:
        raise ValueError("reference_labels cannot be empty.")

    if labels.shape != scores.shape:
        raise ValueError(
            "reference_labels and attribution_scores must have equal length."
        )

    if not np.isin(labels, [0, 1]).all():
        raise ValueError("reference_labels must contain only 0 and 1.")

    if not np.isfinite(scores).all():
        raise ValueError("attribution_scores must contain only finite values.")

    if not np.isfinite(threshold):
        raise ValueError("threshold must be finite.")

    predicted_labels = (scores >= threshold).astype(int)

    accuracy = accuracy_score(labels, predicted_labels)
    f1 = f1_score(labels, predicted_labels, zero_division=0)

    if np.unique(labels).size < 2:
        auroc = float("nan")
    else:
        auroc = roc_auc_score(labels, scores)

    return AttributionResult(
        accuracy=float(accuracy),
        f1=float(f1),
        auroc=float(auroc),
        threshold=float(threshold),
    )
