
def maximum_circular_subarray(nums):
    if not nums:
        return 0

    total = sum(nums)

    # Normal maximum subarray
    max_current = max_sum = nums[0]

    # Minimum subarray
    min_current = min_sum = nums[0]

    for num in nums[1:]:

        max_current = max(num, max_current + num)
        max_sum = max(max_sum, max_current)

        min_current = min(num, min_current + num)
        min_sum = min(min_sum, min_current)

    # If all numbers are negative
    if max_sum < 0:
        return max_sum

    # Maximum circular sum
    return max(max_sum, total - min_sum)


print(maximum_circular_subarray([5, -3, 5]))
print(maximum_circular_subarray([1, -2, 3, -2]))
print(maximum_circular_subarray([-3, -2, -3]))
