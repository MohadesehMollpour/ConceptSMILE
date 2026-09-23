# Provenance: RECONSTRUCTED reusable code; historical execution not established.
"""Set-overlap stability metric described in the manuscript."""

from __future__ import annotations

from collections.abc import Hashable, Iterable


def jaccard_index(original: Iterable[Hashable], modified: Iterable[Hashable]) -> float:
    """Return Jaccard overlap, treating two empty sets as perfectly stable."""
    original_set = set(original)
    modified_set = set(modified)
    union = original_set | modified_set
    return 1.0 if not union else len(original_set & modified_set) / len(union)
