import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here w coefficient/parameters weight
	
    X = np.asarray(X)
    w = np.asarray(w).reshape(-1)    
    y_true = np.asarray(y_true).reshape(-1)

    y_pred = X @ w
    mse = np.mean((y_pred - y_true)**2) 

    # l2 reg ridge mse + alpha ||
    reg = alpha * np.sum(w ** 2)

    return float(mse + reg)
