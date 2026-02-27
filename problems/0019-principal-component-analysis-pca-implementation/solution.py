import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.

    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return

    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    X = np.asarray(data, dtype=float)
    n_samples, n_features = X.shape

    # 1) Standardize (z-score) each feature
    mean = X.mean(axis=0)
    std = X.std(axis=0, ddof=0)
    std = np.where(std == 0, 1.0, std)  # avoid division by zero
    Z = (X - mean) / std

    # 2) Covariance matrix (features x features)
    # sample covariance (divide by n_samples - 1)
    cov = (Z.T @ Z) / (n_samples - 1)

    # 3) Eigen-decomposition (cov is symmetric)
    eigvals, eigvecs = np.linalg.eigh(cov)  # eigvals ascending

    # 4) Sort by descending eigenvalues