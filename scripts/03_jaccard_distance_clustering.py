# 03_jaccard_distance_clustering.py
"""
Compute Jaccard genetic distance, hierarchical clustering, silhouette index,
and cophenetic correlation for ISSR binary data. Saves key outputs to /processed.
"""
import pandas as pd
from scipy.spatial.distance import pdist, squareform
from scipy.cluster.hierarchy import linkage, dendrogram, cophenet
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

def compute_jaccard_and_cluster(issr_matrix):
    dist_array = pdist(issr_matrix.values, metric="jaccard")
    dist_matrix = squareform(dist_array)

    # Save full distance matrix
    df_dist = pd.DataFrame(dist_matrix, index=issr_matrix.index, columns=issr_matrix.index)
    df_dist.to_csv("/content/Tamarindus_ISSR_EC/processed/distance_matrix_jaccard.csv")

    results = {}
    for method in ['average', 'ward', 'complete', 'single']:
        link = linkage(dist_array, method=method)
        coph_corr, _ = cophenet(link, dist_array)
        try:
            leaves_order = dendrogram(link, no_plot=True)['leaves']
            silhouette = silhouette_score(dist_matrix, leaves_order, metric='precomputed') if len(set(leaves_order)) > 1 else None
        except:
            leaves_order = []
            silhouette = None
        results[method] = {"linkage": link, "cophenetic": coph_corr, "silhouette": silhouette}

    # Save dendrogram order for 'average' method
    if 'average' in results:
        leaves_order = dendrogram(results['average']['linkage'], no_plot=True)['leaves']
        ordered = issr_matrix.index[leaves_order]
        pd.DataFrame({'Accession': ordered}).to_csv("/content/Tamarindus_ISSR_EC/processed/dendrogram_coordinates.csv", index=False)

    return dist_matrix, results

if __name__ == "__main__":
    # Asegúrate de tener 'issr_matrix' cargado
    df = pd.read_csv("/content/Tamarindus_ISSR_EC/processed/issr_binary_matrix.csv")
    loci_matrix = df[[str(i) for i in range(1, 33)]].T
    loci_matrix.columns = [f"{row['No']}_bp{int(row['MT'])}" for _, row in df.iterrows()]
    loci_matrix.index = [f"TI-{i:03}" for i in range(1, 33)]
    issr_matrix = loci_matrix.astype(int)

    compute_jaccard_and_cluster(issr_matrix)