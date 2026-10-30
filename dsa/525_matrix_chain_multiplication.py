
def matrix_chain_multiplication(dimensions):
    n = len(dimensions) - 1

    if n <= 0:
        return 0

    # dp[i][j] = minimum multiplication cost
    dp = [[0] * n for _ in range(n)]

    # Length of matrix chain
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            dp[i][j] = float("inf")

            # Try every possible splitting point
            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]


print(matrix_chain_multiplication([10, 30, 5, 60]))
print(matrix_chain_multiplication([40, 20, 30, 10, 30]))
print(matrix_chain_multiplication([10, 20]))
