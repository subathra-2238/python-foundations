
def rod_cutting(prices, length):
    # dp[i] = maximum profit for rod length i
    dp = [0] * (length + 1)

    for current_length in range(1, length + 1):

        for cut_length in range(1, current_length + 1):

            price = prices[cut_length - 1]

            dp[current_length] = max(
                dp[current_length],
                price + dp[current_length - cut_length]
            )

    return dp[length]


print(rod_cutting([2, 5, 7, 8], 4))
print(rod_cutting([1, 5, 8, 9, 10, 17, 17, 20], 8))
print(rod_cutting([3, 5, 8], 3))
