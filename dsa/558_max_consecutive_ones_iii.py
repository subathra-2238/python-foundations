
def longest_ones(nums, k):
    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1

            left += 1

        current_length = right - left + 1
        max_length = max(max_length, current_length)

    return max_length


print(longest_ones([1, 1, 0, 0, 1, 1, 1, 0], 2))
print(longest_ones([1, 0, 1, 1, 0, 1], 1))
print(longest_ones([1, 1, 1, 1], 2))
print(longest_ones([0, 0, 0], 0))
print(longest_ones([], 2))
