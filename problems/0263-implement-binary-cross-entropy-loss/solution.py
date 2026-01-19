import math
def binary_cross_entropy(y_true: list[float], y_pred: list[float], epsilon: float = 1e-15) -> float:
	total = 0.0
	n = len(y_true)

	for y,p in zip(y_true, y_pred):
		p = max(epsilon , min(1.0 - epsilon, p))
		total += -(y * math.log(p) + (1 - y) * math.log(1 - p))

	return total / n

	# total = 0.0
    # n = len(y_true)

    # for y, p in zip(y_true, y_pred):
    #     # clip for numerical stability
    #     p = max(epsilon, min(1.0 - epsilon, p))
    #     total += -(y * math.log(p) + (1 - y) * math.log(1 - p))

    # return total / n