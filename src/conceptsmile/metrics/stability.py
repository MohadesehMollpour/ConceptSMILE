"""ConceptSMILE stability metric.

Manuscript correspondence:
    Eq. (17)

Stability is measured using the Jaccard overlap between
the original explanation set and the explanation obtained
after adding a superficial non-clinical artefact.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable

from dataclasses import dataclass


@dataclass(frozen=True)
class StabilityMetrics:
    """Stability evaluation result."""

    jaccard: float
    intersection_size: int
    union_size: int


def evaluate_stability(
    original_explanation: Iterable[Hashable],
    modified_explanation: Iterable[Hashable],
) -> StabilityMetrics:
    """Evaluate explanation stability using Eq. (17).

    Parameters
    ----------
    original_explanation:
        Explanation set A for the original image.

    modified_explanation:
        Explanation set B after adding an artefact,
        such as a date or logo.

    Returns
    -------
    StabilityMetrics
        Jaccard overlap and the corresponding
        intersection and union sizes.
    """

    original_set = set(original_explanation)
    modified_set = set(modified_explanation)

    intersection = original_set & modified_set
    union = original_set | modified_set

    if len(union) == 0:
        raise ValueError(
            "Jaccard stability is undefined when "
            "both explanation sets are empty."
        )

    jaccard = len(intersection) / len(union)

    return StabilityMetrics(
        jaccard=float(jaccard),
        intersection_size=len(intersection),
        union_size=len(union),
    )


def jaccard_index(
    original_explanation: Iterable[Hashable],
    modified_explanation: Iterable[Hashable],
) -> float:
    """Return only the Jaccard stability value."""

    return evaluate_stability(
        original_explanation,
        modified_explanation,
    ).jaccard
