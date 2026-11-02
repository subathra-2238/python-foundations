
def min_operations(nums, x):
    total = sum(nums)
    target = total - x

    if target < 0:
        return -1

    if target == 0:
        return len(nums)

    left = 0
    current_sum = 0
    max_length = -1

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > target and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == target:
            max_length = max(max_length, right - left + 1)

    if max_length == -1:
        return -1

    return len(nums) - max_length


print(min_operations([1, 1, 4, 2, 3], 5))
print(min_operations([5, 6, 7, 8, 9], 4))
print(min_operations([3, 2, 20, 1, 1, 3], 10))
print(min_operations([1, 1], 3))
