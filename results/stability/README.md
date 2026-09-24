"""ConceptSMILE stability metric.

Paper Eq. (17):
J(A, B) = |A intersection B| / |A union B|
"""


def jaccard_stability(original_explanation, modified_explanation):
    original = set(original_explanation)
    modified = set(modified_explanation)

    union = original | modified

    if len(union) == 0:
        raise ValueError(
            "Jaccard index is undefined when both "
            "explanation sets are empty."
        )

    intersection = original & modified

    return len(intersection) / len(union)
