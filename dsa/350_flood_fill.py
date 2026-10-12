matrix = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

start_row = 0
start_column = 0
new_value = 2

old_value = matrix[start_row][start_column]

if old_value != new_value:
    stack = [(start_row, start_column)]
    matrix[start_row][start_column] = new_value

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while stack:
        row, column = stack.pop()

        for dr, dc in directions:
            new_row = row + dr
            new_column = column + dc

            if (
                0 <= new_row < len(matrix)
                and 0 <= new_column < len(matrix[0])
                and matrix[new_row][new_column] == old_value
            ):
                matrix[new_row][new_column] = new_value
                stack.append((new_row, new_column))

print("Matrix after flood fill:")

for row in matrix:
    print(row)
