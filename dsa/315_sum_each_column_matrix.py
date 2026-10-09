matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

columns = len(matrix[0])

for j in range(columns):
    column_sum = 0

    for i in range(len(matrix)):
        column_sum += matrix[i][j]

    print("Column sum:", column_sum)
