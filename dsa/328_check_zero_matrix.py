matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

zero_matrix = True

for row in matrix:
    for number in row:
        if number != 0:
            zero_matrix = False
            break

    if not zero_matrix:
        break

if zero_matrix:
    print("Matrix is a zero matrix")
else:
    print("Matrix is not a zero matrix")
