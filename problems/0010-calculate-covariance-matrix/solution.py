def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
    n= len(vectors[0]) # number of observation, sample ,len(a[0])  # number of columns → 3
    m = len(vectors) # number of feature, row len(a) # number of rows → 2

    means = [sum(v)/n for v in vectors]

    cov_matrix = [ [0 for _ in range(m)] for _ in range(m)]
    for i in range(m):
        for j in range(m):
            cov_ij = sum( 
                (vectors[i][k] - means[i]) * (vectors[j][k] - means[j])
                for k in range(n)
            )/ (n-1)
            cov_matrix [i][j]= round(cov_ij,2)
	return cov_matrix