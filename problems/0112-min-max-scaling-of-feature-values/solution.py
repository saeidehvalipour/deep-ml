def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    """

    if not x:
        return []

    min_val = min(x)
    max_val = max(x)

    # avoid division by zero when all values are equal
    if min_val == max_val:
        return [0.0 for _ in x]

    return [(val - min_val) / (max_val - min_val) for val in x]
