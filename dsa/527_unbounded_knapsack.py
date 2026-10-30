
def unbounded_knapsack(weights, values, capacity):
    # dp[w] = maximum value for capacity w
    dp = [0] * (capacity + 1)

    for current_capacity in range(1, capacity + 1):

        for i in range(len(weights)):

            if weights[i] <= current_capacity:

                dp[current_capacity] = max(
                    dp[current_capacity],
                    values[i] + dp[current_capacity - weights[i]]
                )

    return dp[capacity]


print(unbounded_knapsack([2, 3, 4], [4, 5, 7], 8))
print(unbounded_knapsack([1, 2], [10, 15], 3))
print(unbounded_knapsack([3, 4], [5, 7], 2))
