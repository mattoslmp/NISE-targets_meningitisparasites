# NISE-targets_meningitisparasites

Comparative AnEnPi-derived catalog of non-homologous isofunctional enzyme candidates in neurotropic and neurologically relevant helminths.

## Authors

Leandro de Mattos Pereira^1,2,*, Carlos Graeff-Teixeira^3,4 and Alessandra Loureiro Morassutti^4.

1 Instituto Tecnológico Vale (ITV), Belém, Pará, Brazil.
2 Databiomics, Bioinformatics and Data Science Laboratory, WBPEREIRA, Avenida Coronel José Bastos 700, Aeroporto, Itaperuna, Rio de Janeiro, Brazil.
3 Universidade Federal do Espírito Santo, ES, Brazil.
4 Universidade de Passo Fundo, Passo Fundo, RS, Brazil.

## GitHub Pages

The final static project page is available as both `index.html` and `docs/index.html` so the site can publish from either the repository root or `/docs`.

Expected public URL:

`https://mattoslmp.github.io/NISE-targets_meningitisparasites/`

If the URL returns 404, configure GitHub Pages in the repository settings:

- Option A: **Settings -> Pages -> Deploy from a branch -> main -> /(root) -> Save**
- Option B: **Settings -> Pages -> Deploy from a branch -> main -> /docs -> Save**
- Option C: **Settings -> Pages -> Source -> GitHub Actions**, then run the workflow `.github/workflows/pages.yml`.

## Final manuscript package

- `manuscript/NISE_targets_meningitisparasites_final_ParasitesVectors_authors_updated.docx`
- `manuscript/NISE_targets_meningitisparasites_final_ParasitesVectors_authors_updated.pdf`
- `manuscript/NISE_targets_supplementary_figures_final.docx`
- `manuscript/NISE_targets_supplementary_figures_final.pdf`
- `tables/NISE_targets_supplementary_tables_final_formatted.xlsx`

## Main results

- 7 parasite datasets parsed.
- 43 curated EC activities prioritized.
- 26 target ECs present as AnEnPi-reconstructed analog candidates in all seven datasets.
- Priority score: `2*n_datasets + evidence_bonus + EC_quality_bonus + sequence_support_bonus`.
- Main target axes: dTMP kinase, APS kinase, ADP-ribosyltransferase, cystathionine gamma-lyase, adenosine deaminase, NUDIX/ADP-ribose hydrolase-like activities and ValRS.

## Data-integrity statement

SUPERFAMILY/SCOP assignment tables were not present in the uploaded package. Fold IDs were therefore not invented. The tables include fold-validation fields and database links so candidates can be promoted to fold-validated NISEs only after sequence-specific structural-superfamily confirmation.
