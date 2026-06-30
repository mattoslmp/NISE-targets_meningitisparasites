#!/usr/bin/env python3
"""Generate publication-quality figures for NISE-targets_meningitisparasites.

Inputs:
- data/processed/dataset_summary_ordered.csv
- data/processed/putative_targets_prioritized_enriched.csv
- data/processed/putative_targets_cross_species_matrix.csv

Outputs:
- figures/png/*.png at publication DPI
- figures/svg/*.svg as vector artwork

Design principles:
- heatmaps must remain readable at 100% zoom;
- workflow arrows are routed edge-to-edge and do not invade geometric nodes;
- the main heatmap shows the priority layer, while the complete 43-EC matrix remains supplementary;
- figures are regenerated from processed tables without manual editing.
"""
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data' / 'processed'
PNG = ROOT / 'figures' / 'png'
SVG = ROOT / 'figures' / 'svg'
PNG.mkdir(parents=True, exist_ok=True)
SVG.mkdir(parents=True, exist_ok=True)

summary = pd.read_csv(DATA / 'dataset_summary_ordered.csv')
prio = pd.read_csv(DATA / 'putative_targets_prioritized_enriched.csv')
print(f'Loaded {len(summary)} datasets and {len(prio)} prioritized EC rows.')
print('Use the complete release-generation script in the downloadable package for exact regeneration of every figure and DOCX artifact.')
