
def split_array(nums, k):
    left = max(nums)
    right = sum(nums)

    while left < right:
        limit = (left + right) // 2

        groups = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > limit:
                groups += 1
                current_sum = 0

            current_sum += num

        if groups <= k:
            right = limit
        else:
            left = limit + 1

    return left


print(split_array([7, 2, 5, 10, 8], 2))
print(split_array([1, 2, 3, 4, 5], 2))
print(split_array([1, 4, 4], 3))
