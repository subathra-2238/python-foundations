def range_bitwise_and(left, right):
    shift = 0

    while left < right:
        left >>= 1
        right >>= 1
        shift += 1

    return left << shift


print("Range [5, 7]:", range_bitwise_and(5, 7))
print("Range [0, 1]:", range_bitwise_and(0, 1))
print("Range [12, 15]:", range_bitwise_and(12, 15))
