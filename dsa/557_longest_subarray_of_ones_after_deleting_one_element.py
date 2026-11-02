
def longest_subarray(nums):
    left = 0
    zero_count = 0
    max_length = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1

            left += 1

        current_length = right - left + 1

        # Subtract one because exactly one element must be deleted
        max_length = max(max_length, current_length - 1)

    return max_length


print(longest_subarray([1, 1, 0, 1, 1, 1]))
print(longest_subarray([0, 1, 1, 1, 0, 1]))
print(longest_subarray([1, 1, 1]))
print(longest_subarray([0, 0, 0]))
print(longest_subarray([]))
