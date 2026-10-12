matrix = [
    [1, 0],
    [0, 1]
]

n = len(matrix)

transpose = []

for j in range(n):
    row = []

    for i in range(n):
        row.append(matrix[i][j])

    transpose.append(row)

product = []

for i in range(n):
    row = []

    for j in range(n):
        value = 0

        for k in range(n):
            value += matrix[i][k] * transpose[k][j]

        row.append(value)

    product.append(row)

orthogonal = True

for i in range(n):
    for j in range(n):
        expected = 1 if i == j else 0

        if product[i][j] != expected:
            orthogonal = False
            break

if orthogonal:
    print("Matrix is orthogonal")
else:
    print("Matrix is not orthogonal")
