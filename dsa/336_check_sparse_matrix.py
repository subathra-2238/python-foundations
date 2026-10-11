matrix = [
    [0, 0, 3],
    [0, 0, 0],
    [4, 0, 0]
]

rows = len(matrix)
columns = len(matrix[0])

zero_count = 0

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 0:
            zero_count += 1

total_elements = rows * columns

if zero_count > total_elements / 2:
    print("Matrix is a sparse matrix")
else:
    print("Matrix is not a sparse matrix")
