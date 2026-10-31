
# DSA 535: Best Time to Buy and Sell Stock with Cooldown

def max_profit(prices):
    if not prices:
        return 0

    hold = -prices[0]
    sold = 0
    cooldown = 0

    for price in prices[1:]:
        previous_hold = hold
        previous_sold = sold
        previous_cooldown = cooldown

        # Continue holding or buy today
        hold = max(previous_hold, previous_cooldown - price)

        # Sell the stock today
        sold = previous_hold + price

        # Rest today after selling earlier
        cooldown = max(previous_cooldown, previous_sold)

    return max(sold, cooldown)


print(max_profit([1, 2, 3, 0, 2]))
print(max_profit([1]))
print(max_profit([2, 1, 4]))
