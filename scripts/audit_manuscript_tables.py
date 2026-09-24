"""Audit manuscript-transcribed numbers without regenerating experiments.

This script uses only the Python standard library. It performs arithmetic,
cross-table, and traceability checks on manuscript-transcribed result files.
Audit outputs are diagnostic records and must not be interpreted as corrected
experimental results.
"""

from __future__ import annotations

import csv
import json
import math
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "results" / "manuscript_transcribed"
OUT = ROOT / "docs" / "audits"

DISTANCES = ("cosine", "wasserstein")
CROSS_TABLE_NUMBERS = (2, 3, 7)
IDENTITY_FIELDS = ("pathway", "dataset", "concept", "variant")
TABLE4_METRICS = (
    "cosine_r",
    "cosine_Std",
    "cosine_p",
    "wasserstein_r",
    "wasserstein_Std",
    "wasserstein_p",
)

SD_DISPLAY_HALF_UNIT = 0.00000005


def read_table(number: int) -> list[dict[str, str]]:
    """Read one manuscript-transcribed result table."""
    path = TABLES / f"table{number}_manuscript_transcribed.csv"

    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream))


def save_csv(name: str, rows: list[dict[str, Any]]) -> None:
    """Write an audit CSV."""
    if not rows:
        raise ValueError(f"Cannot write empty audit output: {name}")

    path = OUT / name
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=list(rows[0]),
        )
        writer.writeheader()
        writer.writerows(rows)


def rounding_overlap(
    variance: float,
    standard_deviation: float,
    variance_half_unit: float,
) -> bool:
    """Check whether variance and SD intervals can overlap after rounding.

    The printed standard-deviation half-unit is 0.00005 × 10^-3.
    """
    low_variance = max(
        0.0,
        variance - variance_half_unit,
    )
    high_variance = variance + variance_half_unit

    low_sd = max(
        0.0,
        standard_deviation - SD_DISPLAY_HALF_UNIT,
    )
    high_sd = standard_deviation + SD_DISPLAY_HALF_UNIT

    return max(
        low_variance,
        low_sd**2,
    ) <= min(
        high_variance,
        high_sd**2,
    )


def audit_table6() -> None:
    """Audit displayed variance/standard-deviation pairs in Table 6."""
    rows: list[dict[str, Any]] = []

    for source in read_table(6):
        for distance in DISTANCES:
            variance_display = source[
                f"{distance}_variance_display_x1e-4"
            ]
            sd_display = source[
                f"{distance}_std_display_x1e-3"
            ]

            variance = float(variance_display) * 1e-4
            standard_deviation = float(sd_display) * 1e-3

            strict = rounding_overlap(
                variance,
                standard_deviation,
                0.00005 * 1e-4,
            )
            coarse = rounding_overlap(
                variance,
                standard_deviation,
                0.005 * 1e-4,
            )

            if strict:
                status = "CONSISTENT_WITH_PRINTED_ROUNDING"
            elif coarse:
                status = "POSSIBLE_COARSER_ROUNDING_NOT_VERIFIED"
            else:
                status = "INCONSISTENT_UNDER_SINGLE_DISTRIBUTION"

            rows.append(
                {
                    "pathway": source["pathway"],
                    "dataset": source["dataset"],
                    "concept": source["concept"],
                    "distance": distance,
                    "variance_display": variance_display,
                    "sd_display": sd_display,
                    "variance_scale": "1e-4",
                    "sd_scale": "1e-3",
                    "variance_scaled": variance,
                    "sd_scaled": standard_deviation,
                    "sqrt_variance_diagnostic_NOT_CORRECTION": (
                        math.sqrt(variance)
                    ),
                    "sd_squared": standard_deviation**2,
                    "status": status,
                    "scale_or_aggregation_ambiguity": (
                        "Aggregation unit unknown; "
                        "scales printed explicitly"
                    ),
                    "source": "Manuscript Table 6 p31",
                    "provenance": (
                        "MANUSCRIPT-TRANSCRIBED inputs; "
                        "computed arithmetic audit"
                    ),
                    "original_correction_available": (
                        "NOT AVAILABLE; do not replace numbers"
                    ),
                }
            )

    save_csv(
        "table6_variance_sd_audit.csv",
        rows,
    )

    counts = Counter(
        row["status"]
        for row in rows
    )
    print(
        "Table 6:",
        dict(counts),
    )


def collect_cross_table_records() -> list[
    tuple[
        int,
        int,
        dict[str, str],
        str,
        Decimal,
    ]
]:
    """Collect auditable scalar values from Tables 2, 3, and 7."""
    records = []

    for table_number in CROSS_TABLE_NUMBERS:
        for row_id, row in enumerate(
            read_table(table_number)
        ):
            for metric, value in row.items():
                is_fidelity_metric = metric in {
                    "WMSE",
                    "WMAE",
                    "R2",
                    "Rw2",
                }
                is_distance_metric = metric.startswith(
                    ("cosine_", "wasserstein_")
                )

                if is_fidelity_metric or is_distance_metric:
                    records.append(
                        (
                            table_number,
                            row_id,
                            row,
                            metric,
                            Decimal(value),
                        )
                    )

    return records


def audit_cross_table_matches() -> None:
    """Record exact displayed-value matches across different tables.

    Numerical equality alone is not treated as evidence of provenance,
    copying, or common computational origin.
    """
    records = collect_cross_table_records()
    matches: list[dict[str, Any]] = []

    for index, first in enumerate(records):
        for second in records[index + 1 :]:
            if first[0] == second[0]:
                continue

            if first[4] != second[4]:
                continue

            identity_a = "/".join(
                first[2].get(field, "")
                for field in IDENTITY_FIELDS
            )
            identity_b = "/".join(
                second[2].get(field, "")
                for field in IDENTITY_FIELDS
            )

            matches.append(
                {
                    "table_a": first[0],
                    "row_a_zero_based": first[1],
                    "identity_a": identity_a,
                    "metric_a": first[3],
                    "table_b": second[0],
                    "row_b_zero_based": second[1],
                    "identity_b": identity_b,
                    "metric_b": second[3],
                    "exact_display_value": str(first[4]),
                    "interpretation": (
                        "Equal rounded values only; "
                        "intentional/copying NOT ESTABLISHED"
                    ),
                    "original_assembly_source": "NOT AVAILABLE",
                }
            )

    save_csv(
        "cross_table_exact_value_matches.csv",
        matches,
    )


def collect_legacy_plain_text_outputs() -> list[
    tuple[
        str,
        int,
        int,
        str,
    ]
]:
    """Collect retained plain-text outputs from legacy notebooks."""
    outputs = []

    legacy_directory = ROOT / "notebooks" / "legacy"

    for file in sorted(
        legacy_directory.glob("*.ipynb")
    ):
        notebook = json.loads(
            file.read_text(encoding="utf-8")
        )

        for cell_id, cell in enumerate(
            notebook["cells"]
        ):
            for output_id, output in enumerate(
                cell.get("outputs", [])
            ):
                text = output.get(
                    "text",
                    "",
                )
                if isinstance(text, list):
                    text = "".join(text)

                plain = output.get(
                    "data",
                    {},
                ).get(
                    "text/plain",
                    "",
                )
                if isinstance(plain, list):
                    plain = "".join(plain)

                outputs.append(
                    (
                        file.name,
                        cell_id,
                        output_id,
                        text + plain,
                    )
                )

    return outputs


def audit_table4_traceability() -> None:
    """Trace displayed Table 4 values against legacy plain-text outputs.

    Coincidental numerical matches are recorded only as possible matches and
    are explicitly not treated as proof of computational provenance.
    """
    outputs = collect_legacy_plain_text_outputs()
    traces: list[dict[str, Any]] = []

    for row in read_table(4):
        for metric in TABLE4_METRICS:
            value = row[metric]

            pattern = (
                r"(?<![\d.])"
                + re.escape(value)
                + r"(?![\d.])"
            )

            possible_matches = [
                f"{name}:cell{cell_id}:output{output_id}"
                for (
                    name,
                    cell_id,
                    output_id,
                    text,
                ) in outputs
                if re.search(
                    pattern,
                    text,
                )
            ]

            traces.append(
                {
                    "pathway": row["pathway"],
                    "dataset": row["dataset"],
                    "concept": row["concept"],
                    "metric": metric,
                    "value": value,
                    "source": "Table 4 p27",
                    "provenance": "MANUSCRIPT-TRANSCRIBED",
                    "possible_numeric_matches_NOT_PROVENANCE": (
                        ";".join(possible_matches)
                    ),
                    "relevant_code": (
                        "M42"
                        if row["pathway"] == "MedSAM"
                        else "V17,V25"
                    ),
                    "raw_csv_or_array": "NOT AVAILABLE",
                    "computational_regeneration": "NOT ESTABLISHED",
                }
            )

    save_csv(
        "table4_value_traceability.csv",
        traces,
    )

    print(
        "Table 4:",
        len(traces),
        "value records",
    )


def main() -> int:
    """Run all manuscript-transcription audits."""
    audit_table6()
    audit_cross_table_matches()
    audit_table4_traceability()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
