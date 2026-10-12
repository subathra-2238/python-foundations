matrix = [
    [2, 4],
    [1, 2]
]

determinant = (
    matrix[0][0] * matrix[1][1]
    - matrix[0][1] * matrix[1][0]
)

if determinant == 0:
    print("Matrix is singular")
else:
    print("Matrix is non-singular")
