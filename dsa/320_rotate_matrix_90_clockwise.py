matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rows = len(matrix)
columns = len(matrix[0])

rotated = []

for j in range(columns):
    row = []

    for i in range(rows - 1, -1, -1):
        row.append(matrix[i][j])

    rotated.append(row)

print("Original matrix:")
for row in matrix:
    print(row)

print("Matrix after 90 degree clockwise rotation:")
for row in rotated:
    print(row)
