matrix = [
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1]
]

rows = len(matrix)
columns = len(matrix[0])

queue = [(0, 0, 1)]
visited = {(0, 0)}

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

path_length = -1

while queue:
    r, c, distance = queue.pop(0)

    if r == rows - 1 and c == columns - 1:
        path_length = distance
        break

    for dr, dc in directions:
        nr = r + dr
        nc = c + dc

        if (
            0 <= nr < rows
            and 0 <= nc < columns
            and matrix[nr][nc] == 1
            and (nr, nc) not in visited
        ):
            visited.add((nr, nc))
            queue.append((nr, nc, distance + 1))

print("Shortest path length:", path_length)
