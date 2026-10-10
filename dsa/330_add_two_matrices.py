matrix1 = [
    [1, 2, 3],
    [4, 5, 6]
]

matrix2 = [
    [7, 8, 9],
    [10, 11, 12]
]

result = []

for i in range(len(matrix1)):
    row = []

    for j in range(len(matrix1[i])):
        row.append(matrix1[i][j] + matrix2[i][j])

    result.append(row)

print("Result after adding matrices:")

for row in result:
    print(row)
