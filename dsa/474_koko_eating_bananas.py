
import math


def min_eating_speed(piles, h):
    left = 1
    right = max(piles)

    while left < right:
        speed = (left + right) // 2
        hours = 0

        for pile in piles:
            hours += math.ceil(pile / speed)

        if hours <= h:
            right = speed
        else:
            left = speed + 1

    return left


print(min_eating_speed([3, 6, 7, 11], 8))
print(min_eating_speed([30, 11, 23, 4, 20], 5))
print(min_eating_speed([30, 11, 23, 4, 20], 6))
