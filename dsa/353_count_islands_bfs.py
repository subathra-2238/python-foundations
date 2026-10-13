
from collections import deque

matrix = [
    [1, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]

rows = len(matrix)
cols = len(matrix[0])
islands = 0

for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == 1:
            islands += 1
            queue = deque([(i, j)])
            matrix[i][j] = 0

            while queue:
                r, c = queue.popleft()

                for dr, dc in [
                    (-1, 0), (1, 0),
                    (0, -1), (0, 1)
                ]:
                    nr = r + dr
                    nc = c + dc

                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and matrix[nr][nc] == 1
                    ):
                        matrix[nr][nc] = 0
                        queue.append((nr, nc))

print("Number of islands:", islands)
