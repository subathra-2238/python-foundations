
def maximum_subarray_sum(nums):
    if not nums:
        return 0

    current_sum = nums[0]
    maximum_sum = nums[0]

    for i in range(1, len(nums)):

        # Extend the existing subarray or start a new one
        current_sum = max(
            nums[i],
            current_sum + nums[i]
        )

        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum


print(maximum_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(maximum_subarray_sum([1, 2, 3, 4]))
print(maximum_subarray_sum([-5, -2, -8, -1]))
