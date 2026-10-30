
def coin_change_ways(coins, amount):
    # dp[x] = number of ways to make amount x
    dp = [0] * (amount + 1)

    # One way to make zero: choose no coins
    dp[0] = 1

    for coin in coins:
        for current_amount in range(coin, amount + 1):
            dp[current_amount] += dp[current_amount - coin]

    return dp[amount]


print(coin_change_ways([1, 2, 5], 5))
print(coin_change_ways([2], 3))
print(coin_change_ways([1, 2, 3], 4))
