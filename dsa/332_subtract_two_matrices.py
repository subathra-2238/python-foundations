matrix1 = [
    [10, 20, 30],
    [40, 50, 60]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]

result = []

for i in range(len(matrix1)):
    row = []

    for j in range(len(matrix1[i])):
        row.append(matrix1[i][j] - matrix2[i][j])

    result.append(row)

print("Result after subtracting matrices:")

for row in result:
    print(row)
