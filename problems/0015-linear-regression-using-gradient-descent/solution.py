import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    y = y.reshape(-1, 1)              # (m, 1)
    theta = np.zeros((n, 1))          # (n, 1)

    for _ in range(iterations):
        preds = X @ theta             # (m, 1)
        errors = preds - y            # (m, 1)
        grad = (1 / m) * (X.T @ errors)  # (n, 1)
        theta = theta - alpha * grad

    return theta.flatten()
