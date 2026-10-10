matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

identity = True

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            if matrix[i][j] != 1:
                identity = False
        else:
            if matrix[i][j] != 0:
                identity = False

if identity:
    print("Matrix is an identity matrix")
else:
    print("Matrix is not an identity matrix")
