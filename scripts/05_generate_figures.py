# 05_generate_figures_fixed.py
"""
Generate dendrogram and marker performance plots from processed data, with robust feedback.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram

#dist_array = pdist(issr_matrix.values, metric="jaccard")
#link = linkage(dist_array, method="average")


def plot_dendrogram(linkage_matrix, labels, save_path):
    try:
        plt.figure(figsize=(10, 5))
        dendrogram(linkage_matrix, labels=labels, leaf_rotation=90)
        plt.title("UPGMA Dendrogram - ISSR Tamarindus")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"✅ Dendrogram saved to: {save_path}")
    except Exception as e:
        print(f"❌ Error saving dendrogram: {e}")

def plot_pic_vs_mi(summary_df, save_path):
    try:
        plt.figure(figsize=(6, 4))
        sns.scatterplot(x="Mean PIC", y="MI", data=summary_df)
        plt.title("PIC vs MI per Primer")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"✅ PIC vs MI plot saved to: {save_path}")
    except Exception as e:
        print(f"❌ Error saving PIC vs MI plot: {e}")

def plot_issr_heatmap(issr_matrix, save_path):
    try:
        plt.figure(figsize=(12, 6))
        sns.heatmap(issr_matrix, cmap="viridis", cbar=True)
        plt.title("ISSR Binary Matrix Heatmap")
        plt.xlabel("Loci")
        plt.ylabel("Genotypes")
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
        print(f"✅ Heatmap saved to: {save_path}")
    except Exception as e:
        print(f"❌ Error saving heatmap: {e}")

if __name__ == "__main__":
    import os

    processed_dir = "/content/Tamarindus_ISSR_EC/processed"
    figures_dir = "/content/Tamarindus_ISSR_EC/figures"
    os.makedirs(figures_dir, exist_ok=True)

    try:
        print("📁 Loading required files...")

        # Reconstruct ISSR matrix
        df = pd.read_csv(f"{processed_dir}/issr_binary_matrix.csv")
        loci_matrix = df[[str(i) for i in range(1, 33)]].T
        loci_matrix.columns = [f"{row['No']}_bp{int(row['MT'])}" for _, row in df.iterrows()]
        loci_matrix.index = [f"TI-{i:03}" for i in range(1, 33)]
        issr_matrix = loci_matrix.astype(int)

        summary_df = pd.read_csv(f"{processed_dir}/primer_performance_summary.csv")
        print("✅ Data loaded.")
    except Exception as e:
        print(f"❌ Failed to load input files: {e}")
        exit()

    try:
        from scipy.cluster.hierarchy import linkage
        from scipy.spatial.distance import pdist
        dist_array = pdist(issr_matrix.values, metric="jaccard")
        link = linkage(dist_array, method="average")
        plot_dendrogram(link, labels=issr_matrix.index, save_path=f"{figures_dir}/dendrogram.png")
    except Exception as e:
        print(f"⚠️ Could not compute linkage for dendrogram: {e}")

    plot_pic_vs_mi(summary_df, save_path=f"{figures_dir}/primer_pic_vs_mi.png")
    plot_issr_heatmap(issr_matrix, save_path=f"{figures_dir}/heatmap_issr_matrix.png")
