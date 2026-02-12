def compressed_row_sparse_matrix(dense_matrix):
    """
    Convert a dense matrix (list of lists) to CSR format.
    Returns: (values, col_idx, row_ptr)
      - values: all non-zero elements in row-major order
      - col_idx: column index for each value
      - row_ptr: start index of each row in values (length = rows + 1)
    """
    values = []
    col_idx = []
    row_ptr = [0]   # row_ptr[0] همیشه 0 است

    nnz = 0  # number of non-zeros so far

    for row in dense_matrix:
        for j, val in enumerate(row):
            if val != 0:
                values.append(val)
                col_idx.append(j)
                nnz += 1
        row_ptr.append(nnz)  # بعد از هر سطر، تعداد غیرصفرهای تا اینجا

    return values, col_idx, row_ptr
