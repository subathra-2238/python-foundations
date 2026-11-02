
def max_score(cards, k):
    n = len(cards)

    if k < 0 or k > n:
        return 0

    total = sum(cards)

    if k == n:
        return total

    window_size = n - k
    window_sum = sum(cards[:window_size])
    min_window_sum = window_sum

    for right in range(window_size, n):
        window_sum += cards[right]
        window_sum -= cards[right - window_size]

        min_window_sum = min(min_window_sum, window_sum)

    return total - min_window_sum


print(max_score([1, 2, 3, 4, 5, 6, 1], 3))
print(max_score([2, 2, 2], 2))
print(max_score([9, 7, 7, 9, 7, 7, 9], 7))
print(max_score([1, 2, 3], 0))
