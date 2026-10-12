matrix = [
    [1, 1, 0, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

rows = len(matrix)
columns = len(matrix[0])
largest_group = 0

for i in range(rows):
    for j in range(columns):

        if matrix[i][j] == 1:
            stack = [(i, j)]
            matrix[i][j] = 0
            group_size = 0

            while stack:
                r, c = stack.pop()
                group_size += 1

                directions = [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1)
                ]

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < columns
                        and matrix[nr][nc] == 1
                    ):
                        matrix[nr][nc] = 0
                        stack.append((nr, nc))

            if group_size > largest_group:
                largest_group = group_size

print("Largest connected group size:", largest_group)
