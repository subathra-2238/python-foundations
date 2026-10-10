matrix = [
    [5, 0, 0],
    [0, 8, 0],
    [0, 0, 3]
]

diagonal = True

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i != j and matrix[i][j] != 0:
            diagonal = False
            break

    if not diagonal:
        break

if diagonal:
    print("Matrix is a diagonal matrix")
else:
    print("Matrix is not a diagonal matrix")
