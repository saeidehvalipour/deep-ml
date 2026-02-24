import math


def softmax(scores: list[float]) -> list[float]:
    if not scores:
        return []
    
    m = max(scores)
    exp_vals = [math.exp(s - m) for s in scores]
    total = sum(exp_vals)
    return [v / total for v in exp_vals]
