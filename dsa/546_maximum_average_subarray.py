
# DSA 546: Maximum Average Subarray I
# Fixed-Size Sliding Window

def find_max_average(nums, k):
    if k <= 0 or k > len(nums):
        raise ValueError("Invalid window size")

    # Calculate the first window sum
    current_sum = sum(nums[:k])

    maximum_sum = current_sum

    # Slide the window
    for i in range(k, len(nums)):

        # Remove the outgoing element
        current_sum -= nums[i - k]

        # Add the incoming element
        current_sum += nums[i]

        maximum_sum = max(maximum_sum, current_sum)

    return maximum_sum / k


print(find_max_average([1, 12, -5, -6, 50, 3], 4))
print(find_max_average([5], 1))
print(find_max_average([0, 4, 0, 3, 2], 1))
