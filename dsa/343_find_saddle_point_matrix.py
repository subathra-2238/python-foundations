matrix = [
    [3, 4, 5],
    [6, 7, 8],
    [1, 2, 9]
]

found = False

for i in range(len(matrix)):
    row_minimum = matrix[i][0]
    column = 0

    for j in range(1, len(matrix[i])):
        if matrix[i][j] < row_minimum:
            row_minimum = matrix[i][j]
            column = j

    is_saddle = True

    for k in range(len(matrix)):
        if matrix[k][column] > row_minimum:
            is_saddle = False
            break

    if is_saddle:
        print("Saddle point:", row_minimum)
        print("Row:", i + 1)
        print("Column:", column + 1)
        found = True

if not found:
    print("No saddle point found")
