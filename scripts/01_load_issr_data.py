# 01_load_issr_data.py
"""
Load and validate the ISSR binary matrix, genotype metadata, and primer metadata
using repository-relative paths.

This script is portable across local environments, Google Colab, Linux, macOS,
and Windows because it resolves input files relative to the repository root
instead of using absolute paths such as /content/....
"""

from pathlib import Path
import pandas as pd


# Repository root: one level above the scripts/ folder.
# Expected location of this file:
# Tamarindus_ISSR_EC/scripts/01_load_issr_data.py
REPO_ROOT = Path(__file__).resolve().parents[1]

MATRIX_PATH = REPO_ROOT / "processed" / "issr_binary_matrix.csv"
GENO_PATH = REPO_ROOT / "metadata" / "genotype_metadata.csv"
PRIMER_PATH = REPO_ROOT / "metadata" / "primers_metadata.csv"


def _check_required_files(paths: dict[str, Path]) -> None:
    """Raise an informative error if any required input file is missing."""
    missing = [f"{name}: {path}" for name, path in paths.items() if not path.exists()]
    if missing:
        missing_txt = "\n".join(missing)
        raise FileNotFoundError(
            "Missing required input file(s):\n"
            f"{missing_txt}\n\n"
            f"Resolved repository root: {REPO_ROOT}\n"
            "Make sure this script is located inside the repository scripts/ folder."
        )


def load_issr_data() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Load the curated ISSR binary matrix and associated metadata files.

    Returns
    -------
    issr_matrix : pandas.DataFrame
        Curated binary ISSR matrix. The first column is used as the index.
    genotype_metadata : pandas.DataFrame
        Harmonized genotype metadata.
    primer_metadata : pandas.DataFrame
        Primer metadata.
    """
    paths = {
        "ISSR binary matrix": MATRIX_PATH,
        "genotype metadata": GENO_PATH,
        "primer metadata": PRIMER_PATH,
    }

    _check_required_files(paths)

    issr_matrix = pd.read_csv(MATRIX_PATH, index_col=0)
    genotype_metadata = pd.read_csv(GENO_PATH)
    primer_metadata = pd.read_csv(PRIMER_PATH)

    return issr_matrix, genotype_metadata, primer_metadata


def main() -> None:
    """Run a lightweight loading and validation check."""
    issr_matrix, genotype_metadata, primer_metadata = load_issr_data()

    print(f"Repository root: {REPO_ROOT}")
    print(f"ISSR matrix: {issr_matrix.shape}")
    print(f"Genotype metadata: {genotype_metadata.shape}")
    print(f"Primer metadata: {primer_metadata.shape}")

    print("\nISSR matrix preview:")
    print(issr_matrix.head())

    print("\nGenotype metadata preview:")
    print(genotype_metadata.head())

    print("\nPrimer metadata preview:")
    print(primer_metadata.head())


if __name__ == "__main__":
    main()
