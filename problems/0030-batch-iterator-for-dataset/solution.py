import numpy as np

def batch_iterator(X, y=None, batch_size=64):
    """
    Return a list of batches.
    - If y is provided: each batch is [X_batch, y_batch]
    - If y is None: each batch is X_batch
    """
    X = np.asarray(X)
    n = X.shape[0]

    if batch_size <= 0:
        raise ValueError("batch_size must be a positive integer")

    if y is not None:
        y = np.asarray(y)
        if y.shape[0] != n:
            raise ValueError("X and y must have the same number of samples")

    batches = []
    for start in range(0, n, batch_size):
        end = min(start + batch_size, n)
        X_batch = X[start:end].tolist()

        if y is None:
            batches.append(X_batch)
        else:
            y_batch = y[start:end].tolist()
            batches.append([X_batch, y_batch])

    return batches
