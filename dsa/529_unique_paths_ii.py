
def unique_paths_with_obstacles(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Starting point is blocked
    if grid[0][0] == 1:
        return 0

    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = 1

    for i in range(rows):
        for j in range(cols):

            # Cannot enter an obstacle
            if grid[i][j] == 1:
                dp[i][j] = 0

            else:
                if i > 0:
                    dp[i][j] += dp[i - 1][j]

                if j > 0:
                    dp[i][j] += dp[i][j - 1]

    return dp[rows - 1][cols - 1]


grid1 = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

grid2 = [
    [0, 0],
    [1, 0]
]

grid3 = [
    [1, 0],
    [0, 0]
]

print(unique_paths_with_obstacles(grid1))
print(unique_paths_with_obstacles(grid2))
print(unique_paths_with_obstacles(grid3))
