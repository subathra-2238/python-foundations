
def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2

        hours = 0

        for pile in piles:
            # Ceiling division
            hours += (pile + mid - 1) // mid

        if hours <= h:
            right = mid
        else:
            left = mid + 1

    return left


print(min_eating_speed([3, 6, 7, 11], 8))
print(min_eating_speed([30, 11, 23, 4, 20], 5))
print(min_eating_speed([30, 11, 23, 4, 20], 6))
print(min_eating_speed([5], 5))
