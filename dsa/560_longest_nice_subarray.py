
def longest_nice_subarray(nums):
    left = 0
    used_bits = 0
    max_length = 0

    for right in range(len(nums)):
        while (used_bits & nums[right]) != 0:
            used_bits ^= nums[left]
            left += 1

        used_bits |= nums[right]

        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_nice_subarray([1, 3, 8, 48, 10]))
print(longest_nice_subarray([3, 1, 5, 11, 13]))
print(longest_nice_subarray([1, 2, 4, 8]))
print(longest_nice_subarray([7, 7, 7]))
print(longest_nice_subarray([]))
