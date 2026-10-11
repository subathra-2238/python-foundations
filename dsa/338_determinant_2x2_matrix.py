matrix = [
    [4, 7],
    [2, 6]
]

determinant = (
    matrix[0][0] * matrix[1][1]
    - matrix[0][1] * matrix[1][0]
)

print("Matrix:")
for row in matrix:
    print(row)

print("Determinant:", determinant)
