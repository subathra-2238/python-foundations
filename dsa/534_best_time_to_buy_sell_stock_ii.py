
# DSA 534: Best Time to Buy and Sell Stock II

def max_profit(prices):
    total_profit = 0

    for i in range(1, len(prices)):

        # Collect every positive price increase
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]

    return total_profit


print(max_profit([7, 1, 5, 3, 6, 4]))
print(max_profit([1, 2, 3, 4, 5]))
print(max_profit([7, 6, 4, 3, 1]))
