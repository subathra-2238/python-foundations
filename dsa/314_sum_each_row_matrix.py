matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    row_sum = 0

    for number in row:
        row_sum += number

    print("Row sum:", row_sum)
