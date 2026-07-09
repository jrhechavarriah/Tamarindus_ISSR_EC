# Curated ISSR Dataset and Reproducible Python Workflow for Tamarindus indica L.

## Description

This repository contains a derived and curated binary matrix of ISSR markers from 32 genotypes of Tamarindus indica L., along with a fully reproducible Python workflow for genetic diversity and multivariate analysis.

The dataset was derived from the article:

**Sarmiento L, Pérez-Almeida I, Díaz B, Álvarez H, Viera W.** Molecular marker-based characterization of Ecuadorian dry forest tamarind plus trees. *Bioagro*. 2017;29(3):153-162. Available from: https://ve.scielo.org/scielo.php?script=sci_arttext&pid=S1316-33612017000300001. Accessed April 18, 2026.

When using this dataset or its associated scripts, please cite the following:

Hechavarria-Hernandez, J. R., Pérez-Almeida, I., & Vacacela Gomez, C. (2026).
Tamarindus_ISSR_EC: FAIR-curated ISSR dataset and reproducible computational workflow for genetic diversity analysis of Tamarindus indica in Ecuador [Data set]. Zenodo. https://doi.org/10.5281/zenodo.20276986

GitHub Repository: https://github.com/jrhechavarriah/Tamarindus_ISSR_EC

## 👥 Authors

**Jesus Rafael Hechavarria-Hernandez**¹*  
**Iris Pérez-Almeida**¹*  
**Cristian Vacacela Gomez**²*

¹ Universidad Ecotec, Research Department, Samborondón, Guayas, EC092302, Ecuador  
² University of Calabria, Department of Environmental Engineering (DIAm), Rende, Calabria, 87036, Italy  

📧 jhechavarria@ecotec.edu.ec  
📧 iperez@ecotec.edu.ec  
📧 cristianisaac.vacacelagomez@fis.unical.it  

🔗 ORCID  
- [0000-0002-9013-8665](https://orcid.org/0000-0002-9013-8665) – J.R. Hechavarria-Hernandez  
- [0000-0001-5929-892X](https://orcid.org/0000-0001-5929-892X) – I. Pérez-Almeida  
- [0000-0002-9248-9944](https://orcid.org/0000-0002-9248-9944) – C. Vacacela Gomez  

---

## Repository Structure

```
Tamarindus_ISSR_EC/
├── processed/               # Processed data matrices
│   ├── issr_binary_matrix.csv
│   ├── primer_performance_summary.csv
│   ├── distance_matrix_jaccard.csv
│   └── dendrogram_coordinates.csv
│
├── figures/                 # Publication-quality figures
│   ├── pca_plot.png
│   ├── tsne_plot.png
│   ├── umap_plot.png
│   ├── pcoa_plot.png
│   ├── dendrogram.png
│   ├── primer_pic_vs_mi.png
│   └── heatmap_issr_matrix.png
│
├── metadata/                # Marker and genotype metadata
│   ├── genotype_identifier_mapping.csv
│   ├── genotype_metadata.csv
│   └── primers_metadata.csv
│
├── scripts/                 # Computational scripts
│   ├── 01_load_issr_data.py
│   ├── 02_calculate_diversity_metrics.py
│   ├── 03_jaccard_distance_clustering.py
│   ├── 04_multivariate_analysis.py
│   ├── 05_generate_figures.py
│   ├── 06_validate_dataset.py
│   └── 07_package_zip.py
│
├── docs/                    # Project documentation
│   ├── data_dictionary.csv
│   ├── dataset_reuse_notes.md
│   ├── download_and_processing_protocol.md
│   └── environment_info.txt
│
├── run_all.sh               # Unified execution script
├── dataset_metadata.csv     # Metadata about this repository
├── LICENSE
├── CITATION.cff
├── README.md
├── requirements.txt
└── .gitattributes
```

## Reproducibility

To reproduce the full analysis:

```bash
bash run_all.sh
```

Or run individual scripts:

```bash
python scripts/01_load_issr_data.py
python scripts/02_calculate_diversity_metrics.py
python scripts/03_jaccard_distance_clustering.py
python scripts/04_multivariate_analysis.py
python scripts/05_generate_figures.py
python scripts/06_validate_dataset.py
python scripts/07_package_zip.py
```

## Genotype identifier mapping

Some processed analytical files and figures retain sequential working identifiers used during reproducible computation. The canonical genotype identifiers are provided in metadata/genotype_metadata.csv. Cross-file interoperability is ensured through metadata/genotype_identifier_mapping.csv, which links matrix columns, short identifiers, and canonical genotype codes.

## Reuse Potential

This dataset and pipeline can support:

- ISSR marker analysis and optimization
- Genetic diversity and polymorphism analysis
- Visualization of genetic relationships
- Benchmarking of dimensionality reduction techniques
- Reproducible workflows for plant genetic resource management

## Original Study Attribution

Sarmiento L, Pérez-Almeida I, Díaz B, Álvarez H, Viera W. Molecular marker-based characterization of Ecuadorian dry forest tamarind plus trees. Bioagro. 2017;29(3):153-162. Available from: https://ve.scielo.org/scielo.php?script=sci_arttext&pid=S1316-33612017000300001. Accessed April 18, 2026.

## License

This repository is shared under the Creative Commons Attribution 4.0 International (CC BY 4.0) license.
