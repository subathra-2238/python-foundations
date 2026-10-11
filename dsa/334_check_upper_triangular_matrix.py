matrix = [
    [1, 2, 3],
    [0, 4, 5],
    [0, 0, 6]
]

upper_triangular = True

for i in range(len(matrix)):
    for j in range(i):
        if matrix[i][j] != 0:
            upper_triangular = False
            break

    if not upper_triangular:
        break

if upper_triangular:
    print("Matrix is upper triangular")
else:
    print("Matrix is not upper triangular")
