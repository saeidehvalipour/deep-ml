def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    a, b = matrix[0]
    c, d = matrix[1]

    det = a * d - b * c
    if det == 0:   # safer than det == 0 with floats
        return None

    inv_det = 1.0 / det
    inv = [
        [d * inv_det, -b * inv_det],
        [-c * inv_det, a * inv_det]
    ]
    return [[round(x, 4) for x in row] for row in inv]
 


    