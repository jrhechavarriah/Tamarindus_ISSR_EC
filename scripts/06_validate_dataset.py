# 06_validate_dataset.py
"""
Simple script to check file existence and dataset integrity.
"""
from pathlib import Path

# Validación del repositorio Tamarindus_ISSR_EC
REPO_ROOT = Path(__file__).resolve().parents[1]

required_files = [
    "docs/data_dictionary.csv",
    "docs/dataset_reuse_notes.md",
    "docs/download_and_processing_protocol.md",
    "docs/environment_info.txt",

    "figures/dendrogram.png",
    "figures/heatmap_issr_matrix.png",
    "figures/pca_plot.png",
    "figures/pcoa_plot.png",
    "figures/primer_pic_vs_mi.png",
    "figures/tsne_plot.png",
    "figures/umap_plot.png",

    "metadata/genotype_metadata.csv",
    "metadata/primers_metadata.csv",

    "notebooks/Tamarindus_ISSR_Analysis.ipynb",

    "processed/dendrogram_coordinates.csv",
    "processed/distance_matrix_jaccard.csv",
    "processed/issr_binary_matrix.csv",
    "processed/primer_performance_summary.csv",

    "scripts/01_load_issr_data.py",
    "scripts/02_calculate_diversity_metrics.py",
    "scripts/03_jaccard_distance_clustering.py",
    "scripts/04_multivariate_analysis.py",
    "scripts/05_generate_figures.py",
    "scripts/06_validate_dataset.py",
    "scripts/07_package_zip.py",

    "CITATION.cff",
    "LICENSE",
    "README.md",
    "dataset_metadata.csv",
    "requirements.txt",
    "run_all.sh"
]

missing = []

for f in required_files:
    path = REPO_ROOT / f
    if not path.exists():
        missing.append(str(f))

if len(missing) == 0:
    print("✅ Validación del repositorio exitosa.")
    print(f"📁 Ruta base: {REPO_ROOT}")
else:
    print("❌ Faltan", len(missing), "archivos:")
    for m in missing:
        print(f"/content/Tamarindus_ISSR_EC/{m}")
    raise FileNotFoundError("Faltan archivos requeridos en el repositorio.")