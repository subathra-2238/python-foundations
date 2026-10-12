matrix = [
    [1, 0],
    [0, 1]
]

n = len(matrix)

product = []

for i in range(n):
    row = []

    for j in range(n):
        value = 0

        for k in range(n):
            value += matrix[i][k] * matrix[k][j]

        row.append(value)

    product.append(row)

idempotent = True

for i in range(n):
    for j in range(n):
        if product[i][j] != matrix[i][j]:
            idempotent = False
            break

    if not idempotent:
        break

if idempotent:
    print("Matrix is idempotent")
else:
    print("Matrix is not idempotent")
