#!/usr/bin/env python3
"""Add transparent priority-score components and database links.

Priority score = (2 * n_datasets) + evidence_bonus + EC_quality_bonus + sequence_support_bonus.

Evidence bonus:
  4 = direct inhibitor, approved-drug or validated target-class precedent
  3 = strong pathway, cofactor/nucleotide or host-parasite interaction precedent
  2 = broad computational target-class plausibility
  0 = curation-only or insufficient target-class evidence

EC-quality bonus:
  2 = complete accepted four-field EC
  1 = complete but normalisation-sensitive record
  0 = incomplete/transferred EC class

Sequence-support bonus:
  1 = at least one local parasite sequence identifier/FASTA-supported hit available
  0 = no local sequence support in uploaded material
"""
