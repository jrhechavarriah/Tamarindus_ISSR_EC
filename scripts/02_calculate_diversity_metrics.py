# 02_calculate_diversity_metrics.py
"""
Calculate PIC, Marker Index (MI), and % polymorphism per primer,
derived from ISSR binary matrix directly (in expected format).
"""

import pandas as pd
import numpy as np

def calculate_pic(band_freq):
    return 2 * band_freq * (1 - band_freq)

def compute_diversity_metrics(issr_matrix, save_path="/content/Tamarindus_ISSR_EC/processed/primer_performance_summary.csv"):
    # Mapear loci a primers desde nombres de columnas (ej: UBC807_bp2800 → UBC807)
    primer_map = pd.DataFrame({
        "Locus": issr_matrix.columns,
        "Primer Name": [col.split("_bp")[0] for col in issr_matrix.columns]
    })

    summary = []
    for primer in primer_map["Primer Name"].unique():
        loci = primer_map[primer_map["Primer Name"] == primer]["Locus"].values
        loci = [l for l in loci if l in issr_matrix.columns]
        loci_data = issr_matrix[loci]
        polymorphic_loci = loci_data.loc[:, loci_data.nunique() > 1]
        pic_values = [calculate_pic(loci_data[col].mean()) for col in polymorphic_loci.columns]
        mean_pic = np.mean(pic_values) if pic_values else 0
        mi = mean_pic * polymorphic_loci.shape[1]
        summary.append({
            "Primer Name": primer,
            "Total Bands": loci_data.shape[1],
            "Polymorphic Bands": polymorphic_loci.shape[1],
            "% Polymorphism": 100 * polymorphic_loci.shape[1] / loci_data.shape[1] if loci_data.shape[1] > 0 else 0,
            "Mean PIC": round(mean_pic, 3),
            "MI": round(mi, 3)
        })

    df_summary = pd.DataFrame(summary)
    df_summary.to_csv(save_path, index=False)
    print(f"✅ Saved: {save_path}")
    return df_summary
    
if __name__ == "__main__":
    df = pd.read_csv("/content/Tamarindus_ISSR_EC/processed/issr_binary_matrix.csv")
    loci_matrix = df[[str(i) for i in range(1, 33)]].T
    loci_matrix.columns = [f"{row['No']}_bp{int(row['MT'])}" for _, row in df.iterrows()]
    loci_matrix.index = [f"TI-{i:03}" for i in range(1, 33)]
    issr_matrix = loci_matrix.astype(int)

    compute_diversity_metrics(issr_matrix)   

