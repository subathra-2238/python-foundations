
import math


def smallest_divisor(nums, threshold):
    left = 1
    right = max(nums)

    while left < right:
        divisor = (left + right) // 2

        total = 0
        for num in nums:
            total += math.ceil(num / divisor)

        if total <= threshold:
            right = divisor
        else:
            left = divisor + 1

    return left


print(smallest_divisor([1, 2, 5, 9], 6))
print(smallest_divisor([44, 22, 33, 11, 1], 5))
print(smallest_divisor([2, 3, 5, 7, 11], 11))
