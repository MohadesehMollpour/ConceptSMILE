"""ConceptSMILE reliability evaluation metrics.

This package exposes the five evaluation dimensions reported
in the manuscript:

- attribution accuracy
- surrogate fidelity
- faithfulness
- stability
- consistency
"""

from .attribution import AttributionMetrics, evaluate_attribution
from .consistency import (
    ConsistencyMetrics,
    consistency_statistics,
    evaluate_consistency,
)
from .faithfulness import FaithfulnessMetrics, evaluate_faithfulness
from .fidelity import FidelityMetrics, evaluate_fidelity, weighted_mean
from .stability import StabilityMetrics, evaluate_stability, jaccard_index

__all__ = [
    "AttributionMetrics",
    "ConsistencyMetrics",
    "FaithfulnessMetrics",
    "FidelityMetrics",
    "StabilityMetrics",
    "consistency_statistics",
    "evaluate_attribution",
    "evaluate_consistency",
    "evaluate_faithfulness",
    "evaluate_fidelity",
    "evaluate_stability",
    "jaccard_index",
    "weighted_mean",
]
