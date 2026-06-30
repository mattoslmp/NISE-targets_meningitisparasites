#!/usr/bin/env python3
"""Generate publication figures from processed CSV tables.

This script is a compact entry point. The complete publication figures are also included in the downloadable package generated in ChatGPT.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'processed'
FIG = ROOT / 'figures'
(FIG / 'png').mkdir(parents=True, exist_ok=True)
(FIG / 'svg').mkdir(parents=True, exist_ok=True)

summary = pd.read_csv(DATA / 'dataset_summary_ordered.csv')
print(summary[['tag', 'organism_short', 'ec_file_n', 'same_ec_both', 'analog_candidate_ecs']])

fig, ax = plt.subplots(figsize=(11, 6))
x = np.arange(len(summary))
width = 0.25
ax.bar(x-width, summary['ec_file_n'], width, label='ECs in parasite file')
ax.bar(x, summary['same_ec_both'], width, label='same EC in human and parasite')
ax.bar(x+width, summary['analog_candidate_ecs'], width, label='analog candidates')
ax.set_xticks(x)
ax.set_xticklabels(summary['organism_short'], rotation=35, ha='right')
ax.set_ylabel('Number of EC activities')
ax.set_title('Dataset-level EC space and reconstructed analog candidates')
ax.legend(frameon=False)
ax.grid(axis='y', alpha=0.25)
plt.tight_layout()
plt.savefig(FIG / 'Figure_2_dataset_overview_recreated.png', dpi=300)
plt.savefig(FIG / 'Figure_2_dataset_overview_recreated.svg')
