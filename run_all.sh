#!/bin/bash

# Load ISSR data and prepare matrix
python scripts/01_load_issr_data.py

# Calculate diversity metrics and summary
python scripts/02_calculate_diversity_metrics.py

# Compute Jaccard distances and clustering
python scripts/03_jaccard_distance_clustering.py

# Run multivariate analyses (PCA, t-SNE, UMAP, PCoA)
python scripts/04_multivariate_analysis.py

# Generate publication-ready plots
python scripts/05_generate_figures.py

# Validate dataset before packaging
python scripts/06_validate_dataset.py

# Create ZIP package for Zenodo/GitHub upload
python scripts/07_package_zip.py
