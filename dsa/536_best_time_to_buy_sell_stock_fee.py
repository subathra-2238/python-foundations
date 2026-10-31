
# DSA 536: Best Time to Buy and Sell Stock with Transaction Fee

def max_profit(prices, fee):
    if not prices:
        return 0

    cash = 0
    hold = -prices[0]

    for price in prices[1:]:
        previous_cash = cash
        previous_hold = hold

        # Sell the stock and pay the transaction fee
        cash = max(previous_cash, previous_hold + price - fee)

        # Continue holding or buy the stock
        hold = max(previous_hold, previous_cash - price)

    return cash


print(max_profit([1, 3, 2, 8, 4, 9], 2))
print(max_profit([1, 3, 7, 5, 10, 3], 3))
print(max_profit([5, 4, 3, 2, 1], 1))
