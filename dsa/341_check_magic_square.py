matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

n = len(matrix)

target_sum = 0

for j in range(n):
    target_sum += matrix[0][j]

magic = True

# Check rows
for i in range(n):
    row_sum = 0

    for j in range(n):
        row_sum += matrix[i][j]

    if row_sum != target_sum:
        magic = False
        break

# Check columns
if magic:
    for j in range(n):
        column_sum = 0

        for i in range(n):
            column_sum += matrix[i][j]

        if column_sum != target_sum:
            magic = False
            break

# Check main diagonal
if magic:
    diagonal_sum = 0

    for i in range(n):
        diagonal_sum += matrix[i][i]

    if diagonal_sum != target_sum:
        magic = False

# Check secondary diagonal
if magic:
    diagonal_sum = 0

    for i in range(n):
        diagonal_sum += matrix[i][n - 1 - i]

    if diagonal_sum != target_sum:
        magic = False

if magic:
    print("Matrix is a magic square")
else:
    print("Matrix is not a magic square")
