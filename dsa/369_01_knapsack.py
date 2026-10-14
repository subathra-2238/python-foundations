weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7

n = len(weights)
dp = [[0] * (capacity + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    weight = weights[i - 1]
    value = values[i - 1]

    for current_capacity in range(capacity + 1):
        dp[i][current_capacity] = dp[i - 1][current_capacity]

        if weight <= current_capacity:
            dp[i][current_capacity] = max(
                dp[i][current_capacity],
                value + dp[i - 1][current_capacity - weight]
            )

print("Weights:", weights)
print("Values:", values)
print("Capacity:", capacity)
print("Maximum value:", dp[n][capacity])
