# 01_load_issr_data.py
"""
Load and validate ISSR binary matrix, genotype metadata, and primer metadata.
"""
import os
import pandas as pd  # Esta línea es esencial

def load_issr_data():
    paths = {
        "matrix": "/content/Tamarindus_ISSR_EC/processed/issr_binary_matrix.csv",
        "genotypes": "/content/Tamarindus_ISSR_EC/metadata/genotype_metadata.csv",
        "primers": "/content/Tamarindus_ISSR_EC/metadata/primers_metadata.csv"
    }

    for name, path in paths.items():
        if not os.path.exists(path):
            raise FileNotFoundError(f"Missing file: {path}")

    return (
        pd.read_csv(paths["matrix"], index_col=0),
        pd.read_csv(paths["genotypes"]),
        pd.read_csv(paths["primers"])
    )

issr_matrix, genotype_metadata, primer_metadata = load_issr_data()
# Dimensiones
print("ISSR matrix:", issr_matrix.shape)
print("Genotype metadata:", genotype_metadata.shape)
print("Primer metadata:", primer_metadata.shape)

# Vistazo rápido
print("\nISSR matrix preview:")
print(issr_matrix.head())

print("\nGenotype metadata preview:")
print(genotype_metadata.head())

print("\nPrimer metadata preview:")
print(primer_metadata.head())