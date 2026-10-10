matrix = [
    [10, 25, 15],
    [40, 20, 30],
    [5, 35, 45]
]

columns = len(matrix[0])

for j in range(columns):
    maximum = matrix[0][j]

    for i in range(1, len(matrix)):
        if matrix[i][j] > maximum:
            maximum = matrix[i][j]

    print("Maximum element in column:", maximum)
