
def at_most_sum(nums, goal):
    if goal < 0:
        return 0

    left = 0
    current_sum = 0
    count = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > goal:
            current_sum -= nums[left]
            left += 1

        count += right - left + 1

    return count


def num_subarrays_with_sum(nums, goal):
    return at_most_sum(nums, goal) - at_most_sum(nums, goal - 1)


print(num_subarrays_with_sum([1, 0, 1, 0, 1], 2))
print(num_subarrays_with_sum([0, 0, 0, 0], 0))
print(num_subarrays_with_sum([1, 1, 1], 2))
print(num_subarrays_with_sum([1, 0, 1], 5))
