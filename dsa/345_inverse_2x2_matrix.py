matrix = [
    [4, 7],
    [2, 6]
]

a = matrix[0][0]
b = matrix[0][1]
c = matrix[1][0]
d = matrix[1][1]

determinant = a * d - b * c

if determinant == 0:
    print("Matrix does not have an inverse")
else:
    inverse = [
        [d / determinant, -b / determinant],
        [-c / determinant, a / determinant]
    ]

    print("Inverse matrix:")

    for row in inverse:
        print(row)
