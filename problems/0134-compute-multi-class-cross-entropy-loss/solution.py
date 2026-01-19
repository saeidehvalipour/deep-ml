import numpy as np

def compute_cross_entropy_loss(predicted_probs: np.ndarray, true_labels: np.ndarray, epsilon = 1e-15) -> float:
    predicted_probs = np.asarray(predicted_probs, dtype=float)
    true_labels = np.asarray(true_labels, dtype=float)

    predicted_probs = np.clip(predicted_probs,epsilon, 1 - epsilon)

    # cross entropy = -(sum(y * log(p)))
    per_sample_loss = - np.sum(true_labels * np.log(predicted_probs), axis =1)

    return np.mean(per_sample_loss)