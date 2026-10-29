
def rat_in_a_maze(maze):
    n = len(maze)

    if n == 0 or maze[0][0] == 0 or maze[n - 1][n - 1] == 0:
        return []

    result = []
    visited = [[False] * n for _ in range(n)]

    directions = [
        (1, 0, "D"),
        (0, -1, "L"),
        (0, 1, "R"),
        (-1, 0, "U")
    ]

    def backtrack(row, col, path):
        if row == n - 1 and col == n - 1:
            result.append("".join(path))
            return

        visited[row][col] = True

        for dr, dc, move in directions:
            nr = row + dr
            nc = col + dc

            if (0 <= nr < n and 0 <= nc < n
                    and maze[nr][nc] == 1
                    and not visited[nr][nc]):
                path.append(move)
                backtrack(nr, nc, path)
                path.pop()

        visited[row][col] = False

    backtrack(0, 0, [])
    return result


maze1 = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]

maze2 = [
    [1, 0],
    [0, 1]
]

print(rat_in_a_maze(maze1))
print(rat_in_a_maze(maze2))
