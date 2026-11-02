
def at_most_k_distinct(nums, k):
    if k < 0:
        return 0

    left = 0
    count = 0
    frequency = {}

    for right in range(len(nums)):
        frequency[nums[right]] = frequency.get(nums[right], 0) + 1

        while len(frequency) > k:
            left_num = nums[left]
            frequency[left_num] -= 1

            if frequency[left_num] == 0:
                del frequency[left_num]

            left += 1

        count += right - left + 1

    return count


def exactly_k_distinct(nums, k):
    if k <= 0:
        return 0

    return (
        at_most_k_distinct(nums, k)
        - at_most_k_distinct(nums, k - 1)
    )


print(exactly_k_distinct([1, 2, 1, 2, 3], 2))
print(exactly_k_distinct([1, 2, 3], 1))
print(exactly_k_distinct([1, 1, 1], 1))
print(exactly_k_distinct([1, 2, 3], 4))
