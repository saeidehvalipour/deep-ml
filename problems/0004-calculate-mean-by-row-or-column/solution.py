def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if not matrix or not matrix[0]:
        return []
    
    rows, cols = len(matrix), len(matrix[0])

    if mode == "row":
        means = [sum(row) / len(row) for row in matrix]

    elif mode == "column":
        means = []
        for c in range(cols):
            col_sum = 0
            for r in range(rows):
                col_sum += matrix[r][c]
            means.append(col_sum / rows)

    else:
        raise ValueError("mode must be 'row' or 'column'")

    return means
