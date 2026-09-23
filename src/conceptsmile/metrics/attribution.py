# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Attribution accuracy, F1, and AUROC with explicit external references."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score, roc_curve


@dataclass(frozen=True)
class AttributionMetrics:
    accuracy: float
    f1: float
    auroc: float
    threshold: float
    n: int
    status: str


def evaluate_attribution(
    reference_labels: np.ndarray,
    attribution_scores: np.ndarray,
    *,
    sample_weights: np.ndarray | None = None,
    threshold: float | None = None,
) -> AttributionMetrics:
    """Evaluate scores against supplied binary reference labels.

    When no threshold is supplied, the notebook's Youden-J selection is used on
    the same sample. For confirmatory evaluation, determine the threshold on a
    separate validation set and pass it explicitly. The function cannot verify
    reference-label independence; the caller must document that provenance.
    """
    labels = np.asarray(reference_labels).reshape(-1)
    scores = np.asarray(attribution_scores, dtype=float).reshape(-1)
    if len(labels) != len(scores):
        raise ValueError("reference_labels and attribution_scores must have equal length")
    if not np.isin(labels, [0, 1]).all():
        raise ValueError("reference_labels must be binary")
    if not np.isfinite(scores).all():
        raise ValueError("attribution_scores must be finite")
    weights = (None if sample_weights is None
               else np.asarray(sample_weights, dtype=float).reshape(-1))
    if weights is not None and (len(weights) != len(labels) or not np.isfinite(weights).all()
                                or (weights < 0).any() or weights.sum() <= 0):
        raise ValueError("weights must be aligned, finite, nonnegative and have positive sum")
    if not len(labels):
        raise ValueError("reference_labels must be non-empty")
    if threshold is not None and not np.isfinite(threshold):
        raise ValueError("threshold must be finite")
    if len(labels) < 2 or np.unique(labels).size < 2:
        return AttributionMetrics(
            float("nan"),
            float("nan"),
            float("nan"),
            float("nan"),
            len(labels),
            "single_class_or_too_few_samples",
        )

    adaptive_threshold = threshold is None
    auroc = float(roc_auc_score(labels, scores, sample_weight=weights))
    if threshold is None:
        false_positive, true_positive, thresholds = roc_curve(labels, scores, sample_weight=weights)
        threshold = float(thresholds[int(np.argmax(true_positive - false_positive))])
    predicted = (scores >= threshold).astype(int)
    return AttributionMetrics(
        accuracy=float(accuracy_score(labels, predicted, sample_weight=weights)),
        f1=float(f1_score(labels, predicted, sample_weight=weights, zero_division=0)),
        auroc=auroc,
        threshold=float(threshold),
        n=len(labels),
        status="exploratory_same_sample_threshold" if adaptive_threshold else "ok",
    )
