
def minimum_triangle_path(triangle):
    if not triangle:
        return 0

    # Copy the last row
    dp = triangle[-1][:]

    # Move from bottom to top
    for i in range(len(triangle) - 2, -1, -1):

        for j in range(len(triangle[i])):

            dp[j] = triangle[i][j] + min(
                dp[j],
                dp[j + 1]
            )

    return dp[0]


triangle1 = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

triangle2 = [
    [-10]
]

print(minimum_triangle_path(triangle1))
print(minimum_triangle_path(triangle2))
