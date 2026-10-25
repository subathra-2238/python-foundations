
def min_days(bloom_day, m, k):
    if m * k > len(bloom_day):
        return -1

    left = min(bloom_day)
    right = max(bloom_day)

    while left < right:
        day = (left + right) // 2
        bouquets = 0
        flowers = 0

        for bloom in bloom_day:
            if bloom <= day:
                flowers += 1

                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0

        if bouquets >= m:
            right = day
        else:
            left = day + 1

    return left


print(min_days([1, 10, 3, 10, 2], 3, 1))
print(min_days([1, 10, 3, 10, 2], 3, 2))
print(min_days([7, 7, 7, 7, 12, 7, 7], 2, 3))
