
def minimum_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    # DP table
    dp = [[0] * cols for _ in range(rows)]

    dp[0][0] = grid[0][0]

    # Fill the first row
    for j in range(1, cols):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # Fill the first column
    for i in range(1, rows):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill the remaining cells
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = grid[i][j] + min(
                dp[i - 1][j],
                dp[i][j - 1]
            )

    return dp[rows - 1][cols - 1]


grid1 = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

grid2 = [
    [1, 2, 3],
    [4, 5, 6]
]

print(minimum_path_sum(grid1))
print(minimum_path_sum(grid2))
