# 04_multivariate_analysis_final.py
"""
Perform PCA, t-SNE, UMAP, and PCoA on ISSR binary data, saving plots to /figures.
Includes automatic installation of scikit-bio.
"""

try:
    from skbio import DistanceMatrix
    from skbio.stats.ordination import pcoa
except ModuleNotFoundError:
    import sys
    import subprocess
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-bio'])
    from skbio import DistanceMatrix
    from skbio.stats.ordination import pcoa

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import pdist
from scipy.cluster.hierarchy import linkage, dendrogram

# scaled = StandardScaler().fit_transform(issr_matrix)

# UMAP import (inside function)
try:
    import umap
except ImportError:
    umap = None

def run_multivariate_analysis(issr_matrix):
    print("📊 Iniciando análisis multivariado...")
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(issr_matrix)

    # PCA
    pca = PCA(n_components=2)
    pca_result = pca.fit_transform(scaled_data)
    plt.figure()
    sns.scatterplot(x=pca_result[:,0], y=pca_result[:,1])
    plt.title("PCA - ISSR Matrix")
    plt.xlabel("PC1")
    plt.ylabel("PC2")
    plt.savefig("/content/Tamarindus_ISSR_EC/figures/pca_plot.png")
    plt.close()
    print("✅ PCA guardado.")

    # t-SNE
    tsne = TSNE(n_components=2, perplexity=10, random_state=42)
    tsne_result = tsne.fit_transform(scaled_data)
    plt.figure(figsize=(6, 5))
    sns.scatterplot(x=tsne_result[:,0], y=tsne_result[:,1])
    plt.tight_layout(pad=2.0)
    plt.title("t-SNE - ISSR Matrix")
    plt.xlabel("Dim 1")
    plt.ylabel("Dim 2")
    plt.savefig("/content/Tamarindus_ISSR_EC/figures/tsne_plot.png")
    plt.close()

#    tsne = TSNE(n_components=2, perplexity=10, random_state=42)
#    tsne_result = tsne.fit_transform(scaled_data)
#    plt.figure()
#    sns.scatterplot(x=tsne_result[:,0], y=tsne_result[:,1])
#    plt.title("t-SNE - ISSR Matrix")
#    plt.savefig("/content/Tamarindus_ISSR_EC/figures/tsne_plot.png")
#    plt.close()
#    print("✅ t-SNE guardado.")

    # UMAP
    if umap:
        reducer = umap.UMAP(random_state=42)
        umap_result = reducer.fit_transform(scaled_data)
        plt.figure(figsize=(6, 5))
        sns.scatterplot(x=umap_result[:,0], y=umap_result[:,1])
        plt.tight_layout(pad=2.0)
        plt.title("UMAP - ISSR Matrix")
        plt.xlabel("Dim 1")
        plt.ylabel("Dim 2")
        plt.savefig("/content/Tamarindus_ISSR_EC/figures/umap_plot.png")
        plt.close()
    else:
        print("⚠️ UMAP no disponible")

#    if umap:
#        reducer = umap.UMAP(random_state=42)
#        umap_result = reducer.fit_transform(scaled_data)
#        plt.figure()
#        sns.scatterplot(x=umap_result[:,0], y=umap_result[:,1])
#        plt.title("UMAP - ISSR Matrix")
#        plt.savefig("/content/Tamarindus_ISSR_EC/figures/umap_plot.png")
#        plt.close()
#        print("✅ UMAP guardado.")
#    else:
#        print("⚠️ UMAP no instalado, omitiendo.")

    # PCoA
    try:
        import subprocess, sys
        subprocess.check_call([sys.executable, "-m", "pip", "install", "scikit-bio"])
        jaccard_dist = pairwise_distances(issr_matrix.values, metric='jaccard')  # <- CORRECTO
        dm = DistanceMatrix(jaccard_dist, ids=issr_matrix.index.astype(str).tolist())  # <- asegura que los IDs sean strings válidos
        pcoa_result = pcoa(dm)        
        coords = pcoa_result.samples.iloc[:, :2]
        plt.figure()
        sns.scatterplot(x=coords.iloc[:,0], y=coords.iloc[:,1])
        plt.title("PCoA - Jaccard Distance")
        plt.savefig("/content/Tamarindus_ISSR_EC/figures/pcoa_plot.png")
        plt.close()
        print("✅ PCoA guardado.")
    except Exception as e:
        print(f"⚠️ Error en PCoA:", e)


if __name__ == "__main__":
    print("📁 Cargando matriz binaria ISSR...")
    os.makedirs("/content/Tamarindus_ISSR_EC/figures", exist_ok=True)
    df = pd.read_csv("/content/Tamarindus_ISSR_EC/processed/issr_binary_matrix.csv")
    loci_matrix = df[[str(i) for i in range(1, 33)]].T
    loci_matrix.columns = [f"{row['No']}_bp{int(row['MT'])}" for _, row in df.iterrows()]
    loci_matrix.index = [f"TI-{i:03}" for i in range(1, 33)]
    issr_matrix = loci_matrix.astype(int)
    print("✅ Matriz ISSR cargada con forma:", issr_matrix.shape)
    run_multivariate_analysis(issr_matrix)
