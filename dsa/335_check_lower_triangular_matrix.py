matrix = [
    [1, 0, 0],
    [4, 5, 0],
    [7, 8, 9]
]

lower_triangular = True

for i in range(len(matrix)):
    for j in range(i + 1, len(matrix)):
        if matrix[i][j] != 0:
            lower_triangular = False
            break

    if not lower_triangular:
        break

if lower_triangular:
    print("Matrix is lower triangular")
else:
    print("Matrix is not lower triangular")
