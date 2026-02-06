import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X, dtype=float)
    y = np.array(y, dtype=float)

    XtX = X.T @ X
    Xty = X.T @ y

    try:
        theta = np.linalg.inv(XtX) @ Xty   # normal equation
    except np.linalg.LinAlgError:
        theta = np.linalg.pinv(X) @ y      # fallback

    rounded = np.round(theta, 4)

    # Preserve -0.0 if the ORIGINAL theta was negative but rounding made it 0.0
    for i in range(len(rounded)):
        if rounded[i] == 0.0 and np.signbit(theta[i]):
            rounded[i] = -0.0

    return [float(v) for v in rounded]
