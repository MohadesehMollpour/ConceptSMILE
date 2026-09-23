"""Audit transcribed numbers, not regenerate experiments. Standard library only."""
from __future__ import annotations

import csv
import json
import math
from collections import Counter
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / 'results/manuscript_transcribed'
OUT = ROOT / 'docs/audits'


def read(number):
    with (TABLES / f'table{number}_manuscript_transcribed.csv').open() as stream:
        return list(csv.DictReader(stream))


def save(name, rows):
    with (OUT / name).open('w', newline='') as stream:
        writer = csv.DictWriter(stream, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def rounding_overlap(v, s, variance_half_unit):
    """Compare possible intervals; printed SD half-unit is 0.00005 × 10^-3."""
    low_v, high_v = max(0, v - variance_half_unit), v + variance_half_unit
    low_s, high_s = max(0, s - 0.00000005), s + 0.00000005
    return max(low_v, low_s**2) <= min(high_v, high_s**2)


def main():
    rows = []
    for source in read(6):
        for distance in ['cosine', 'wasserstein']:
            vd = source[f'{distance}_variance_display_x1e-4']
            sd = source[f'{distance}_std_display_x1e-3']
            v, s = float(vd) * 1e-4, float(sd) * 1e-3
            strict = rounding_overlap(v, s, 0.00005 * 1e-4)
            coarse = rounding_overlap(v, s, 0.005 * 1e-4)
            status = ('CONSISTENT_WITH_PRINTED_ROUNDING' if strict else
                      'POSSIBLE_COARSER_ROUNDING_NOT_VERIFIED' if coarse else
                      'INCONSISTENT_UNDER_SINGLE_DISTRIBUTION')
            rows.append({
                'pathway': source['pathway'], 'dataset': source['dataset'],
                'concept': source['concept'], 'distance': distance,
                'variance_display': vd, 'sd_display': sd,
                'variance_scale': '1e-4', 'sd_scale': '1e-3',
                'variance_scaled': v, 'sd_scaled': s,
                'sqrt_variance_diagnostic_NOT_CORRECTION': math.sqrt(v),
                'sd_squared': s * s, 'status': status,
                'scale_or_aggregation_ambiguity': (
                    'Aggregation unit unknown; scales printed explicitly'),
                'source': 'Manuscript Table 6 p31',
                'provenance': 'MANUSCRIPT-TRANSCRIBED inputs; computed arithmetic audit',
                'original_correction_available': 'NOT AVAILABLE; do not replace numbers',
            })
    save('table6_variance_sd_audit.csv', rows)
    print('Table 6:', dict(Counter(r['status'] for r in rows)))

    # All exact scalar matches across different tables. Equality is not provenance.
    records = []
    for n in [2, 3, 7]:
        for row_id, row in enumerate(read(n)):
            for metric, value in row.items():
                if metric in ['WMSE', 'WMAE', 'R2', 'Rw2'] or metric.startswith(
                    ('cosine_', 'wasserstein_')
                ):
                    records.append((n, row_id, row, metric, Decimal(value)))
    matches = []
    for i, a in enumerate(records):
        for b in records[i + 1:]:
            if a[0] == b[0] or a[4] != b[4]:
                continue
            matches.append({
                'table_a': a[0], 'row_a_zero_based': a[1],
                'identity_a': '/'.join(a[2].get(k, '') for k in
                                     ['pathway', 'dataset', 'concept', 'variant']),
                'metric_a': a[3], 'table_b': b[0], 'row_b_zero_based': b[1],
                'identity_b': '/'.join(b[2].get(k, '') for k in
                                     ['pathway', 'dataset', 'concept', 'variant']),
                'metric_b': b[3], 'exact_display_value': str(a[4]),
                'interpretation': 'Equal rounded values only; intentional/copying NOT ESTABLISHED',
                'original_assembly_source': 'NOT AVAILABLE',
            })
    save('cross_table_exact_value_matches.csv', matches)

    # Trace every Table 4 cell without treating coincidental numeric matches as provenance.
    outputs = []
    for file in sorted((ROOT / 'notebooks/legacy').glob('*.ipynb')):
        nb = json.loads(file.read_text())
        for cell_id, cell in enumerate(nb['cells']):
            for output_id, output in enumerate(cell.get('outputs', [])):
                text = output.get('text', '')
                text = ''.join(text) if isinstance(text, list) else text
                plain = output.get('data', {}).get('text/plain', '')
                plain = ''.join(plain) if isinstance(plain, list) else plain
                outputs.append((file.name, cell_id, output_id, text + plain))
    traces = []
    import re
    for row in read(4):
        for metric in ['cosine_r', 'cosine_Std', 'cosine_p',
                       'wasserstein_r', 'wasserstein_Std', 'wasserstein_p']:
            value = row[metric]
            matches = [f'{n}:cell{c}:output{o}' for n, c, o, text in outputs
                       if re.search(r'(?<![\d.])' + re.escape(value) + r'(?![\d.])', text)]
            traces.append({
                'pathway': row['pathway'], 'dataset': row['dataset'],
                'concept': row['concept'], 'metric': metric, 'value': value,
                'source': 'Table 4 p27', 'provenance': 'MANUSCRIPT-TRANSCRIBED',
                'possible_numeric_matches_NOT_PROVENANCE': ';'.join(matches),
                'relevant_code': 'M42' if row['pathway'] == 'MedSAM' else 'V17,V25',
                'raw_csv_or_array': 'NOT AVAILABLE',
                'computational_regeneration': 'NOT ESTABLISHED',
            })
    save('table4_value_traceability.csv', traces)
    print('Table 4:', len(traces), 'value records')


if __name__ == '__main__':
    main()
