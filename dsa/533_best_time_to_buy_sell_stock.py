
# DSA 533: Best Time to Buy and Sell Stock

def max_profit(prices):
    if not prices:
        return 0

    minimum_price = prices[0]
    maximum_profit = 0

    for price in prices:

        # Find the lowest buying price
        minimum_price = min(minimum_price, price)

        # Calculate profit if sold today
        profit = price - minimum_price

        # Update maximum profit
        maximum_profit = max(maximum_profit, profit)

    return maximum_profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([7, 6, 4, 3, 1]))
print(max_profit([2, 4, 1]))
