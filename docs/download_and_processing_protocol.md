# Download and Processing Protocol for Tamarindus_ISSR_EC

This protocol describes the steps required to download, process, and analyze the binary ISSR data generated from *Tamarindus indica* genotypes collected in Ecuador.

---

## 📁 Project Overview

This repository provides a reproducible pipeline to process and analyze ISSR molecular marker data. It includes genotype and primer metadata, binary matrix cleanup, diversity metric calculations, distance-based clustering, multivariate analysis (PCA, t-SNE, UMAP, PCoA), and final packaging for FAIR sharing.

---

## 📄 Original Dataset Details

Geographic metadata (latitude, longitude, and elevation) for each accession were manually extracted from Table 1 of the original publication:

Sarmiento L, Pérez-Almeida I, Díaz B, Álvarez H, Viera W. *Molecular marker-based characterization of Ecuadorian dry forest tamarind plus trees*. Bioagro. 2017;29(3):153–162. Available from: [https://ve.scielo.org/scielo.php?script=sci_arttext&pid=S1316-33612017000300001](https://ve.scielo.org/scielo.php?script=sci_arttext&pid=S1316-33612017000300001)

This extraction was performed manually to ensure completeness of the genotype metadata and to support reuse under FAIR principles.


---

## 🚀 Processing Pipeline

The following processing steps are executed in order:

1. **Loading raw matrix and metadata**  
   Files: `processed/issr_binary_matrix.csv`, `metadata/genotype_metadata.csv`, `metadata/primers_metadata.csv`

2. **Calculating diversity metrics per primer**  
   Script: `scripts/02_calculate_diversity_metrics.py`  
   Output: `processed/primer_performance_summary.csv`

3. **Computing Jaccard distances and clustering**  
   Script: `scripts/03_jaccard_distance_clustering.py`  
   Outputs:  
   - `processed/distance_matrix_jaccard.csv`  
   - `processed/dendrogram_coordinates.csv`

4. **Multivariate analysis (PCA, t-SNE, UMAP, PCoA)**  
   Script: `scripts/04_multivariate_analysis.py`  
   Figures saved to `figures/`

5. **Summary figures**  
   Script: `scripts/05_generate_figures.py`  
   Output figures: dendrogram, heatmap, and primer performance plots.

6. **Validation and final ZIP packaging**  
   Scripts:  
   - `scripts/06_validate_dataset.py`  
   - `scripts/07_package_zip.py`

---

## 🧾 Output Files

All outputs are saved into the following directories:

- `processed/`: CSV files with cleaned matrices and computed statistics
- `figures/`: High-resolution publication-ready plots
- `metadata/`: Curated genotype and primer annotations
- `docs/`: Data dictionary, protocol, environment specs

---

## 📌 Requirements

All scripts are compatible with Python ≥3.8 and the environment specified in `requirements.txt`.

For convenience, a full environment snapshot is stored in `docs/environment_info.txt`.

---

## ✅ Reproducibility

You can reproduce the full analysis by running:

```bash
bash run_all.sh
```

This command sequentially executes all relevant scripts under `/scripts`.

---