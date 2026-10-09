matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rows = len(matrix)
columns = len(matrix[0])

print("Boundary elements:")

# Top row
for j in range(columns):
    print(matrix[0][j], end=" ")

# Right column
for i in range(1, rows):
    print(matrix[i][columns - 1], end=" ")

# Bottom row
for j in range(columns - 2, -1, -1):
    print(matrix[rows - 1][j], end=" ")

# Left column
for i in range(rows - 2, 0, -1):
    print(matrix[i][0], end=" ")
