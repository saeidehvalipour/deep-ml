import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    # Convert to numpy array (float) for stable math
    g = np.asarray(gradient, dtype=float)

    # L2 norm (magnitude)
    mag = float(np.linalg.norm(g))

    # Handle zero-gradient edge case
    if mag == 0.0:
        zeros = [0.0] * len(g)
        return {
            "magnitude": 0.0,
            "direction": zeros,
            "descent_direction": zeros,
        }

    # Unit vectors
    direction = (g / mag).tolist()
    descent_direction = (-g / mag).tolist()

    return {
        "magnitude": mag,
        "direction": direction,
        "descent_direction": descent_direction,
    }

