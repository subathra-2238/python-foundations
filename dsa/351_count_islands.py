
matrix = [
    [1, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 0, 0]
]

rows = len(matrix)
columns = len(matrix[0])
islands = 0

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 1:
            islands += 1
            stack = [(i, j)]
            matrix[i][j] = 0

            while stack:
                r, c = stack.pop()

                for dr, dc in [
                    (-1, 0), (1, 0),
                    (0, -1), (0, 1)
                ]:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < columns
                        and matrix[nr][nc] == 1
                    ):
                        matrix[nr][nc] = 0
                        stack.append((nr, nc))

print("Number of islands:", islands)
