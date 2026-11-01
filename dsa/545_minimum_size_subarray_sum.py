
# DSA 545: Minimum Size Subarray Sum
# Sliding Window Algorithm

def min_subarray_length(target, nums):
    left = 0
    current_sum = 0
    minimum_length = float("inf")

    for right in range(len(nums)):
        current_sum += nums[right]

        # Shrink the window while sum is sufficient
        while current_sum >= target:
            window_length = right - left + 1

            minimum_length = min(
                minimum_length,
                window_length
            )

            current_sum -= nums[left]
            left += 1

    if minimum_length == float("inf"):
        return 0

    return minimum_length


print(min_subarray_length(7, [2, 3, 1, 2, 4, 3]))
print(min_subarray_length(4, [1, 4, 4]))
print(min_subarray_length(11, [1, 1, 1, 1, 1]))
