matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]

equal = True

if len(matrix1) != len(matrix2):
    equal = False
else:
    for i in range(len(matrix1)):
        if len(matrix1[i]) != len(matrix2[i]):
            equal = False
            break

        for j in range(len(matrix1[i])):
            if matrix1[i][j] != matrix2[i][j]:
                equal = False
                break

        if not equal:
            break

if equal:
    print("Matrices are equal")
else:
    print("Matrices are not equal")
