def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    if not a:
        return []

    transposed = [list(row) for row in zip(*a)]    
	return transposed