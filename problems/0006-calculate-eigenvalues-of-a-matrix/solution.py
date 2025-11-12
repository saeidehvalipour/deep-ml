def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    a, b = matrix[0]
    c, d = matrix[1]
    
    # Calculate trace and determinant
    trace = a + d
    determinant = a * d - b * c

    # Discriminant of the quadratic equation
    discriminant = (trace ** 2 - 4 * determinant) ** 0.5

    # Compute eigenvalues
    eigen1 = (trace + discriminant) / 2
    eigen2 = (trace - discriminant) / 2

    # Return as a list sorted from highest to lowest
    return sorted([eigen1, eigen2], reverse=True)