
def coin_change(coins, amount):
    # dp[x] = minimum coins needed to make amount x
    infinity = amount + 1
    dp = [infinity] * (amount + 1)

    # Zero coins are needed to make amount zero
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    1 + dp[current_amount - coin]
                )

    # Check whether the amount can be formed
    if dp[amount] == infinity:
        return -1

    return dp[amount]


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([1, 3, 4], 6))
