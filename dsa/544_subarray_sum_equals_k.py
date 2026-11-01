
# DSA 544: Subarray Sum Equals K

def subarray_sum(nums, k):
    prefix_sum = 0
    count = 0

    # Store prefix sums and their frequencies
    prefix_frequency = {0: 1}

    for num in nums:
        prefix_sum += num

        # Check whether a previous prefix sum exists
        # that makes the current subarray sum equal to k
        required = prefix_sum - k

        if required in prefix_frequency:
            count += prefix_frequency[required]

        # Store the current prefix sum
        prefix_frequency[prefix_sum] = (
            prefix_frequency.get(prefix_sum, 0) + 1
        )

    return count


print(subarray_sum([1, 1, 1], 2))
print(subarray_sum([1, 2, 3], 3))
print(subarray_sum([1, -1, 0], 0))
