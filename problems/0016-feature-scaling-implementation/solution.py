import numpy as np

def feature_scaling(data: np.ndarray):
    # Standardization (z-score)
    mean = np.mean(data, axis=0)
    std = np.std(data, axis=0)
    standardized_data = (data - mean) / std

    # Min-Max normalization
    min_val = np.min(data, axis=0)
    max_val = np.max(data, axis=0)
    normalized_data = (data - min_val) / (max_val - min_val)

    # Round to 4 decimals
    standardized_data = np.round(standardized_data, 4)
    normalized_data = np.round(normalized_data, 4)

    # ⭐ convert to python lists (important!)
    return standardized_data.tolist(), normalized_data.tolist()
