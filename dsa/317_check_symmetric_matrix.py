matrix = [
    [1, 2, 3],
    [2, 4, 5],
    [3, 5, 6]
]

symmetric = True

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] != matrix[j][i]:
            symmetric = False
            break

    if not symmetric:
        break

if symmetric:
    print("Matrix is symmetric")
else:
    print("Matrix is not symmetric")
