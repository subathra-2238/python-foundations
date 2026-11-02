
def at_most_k_odds(nums, k):
    if k < 0:
        return 0

    left = 0
    odd_count = 0
    count = 0

    for right in range(len(nums)):
        if nums[right] % 2 != 0:
            odd_count += 1

        while odd_count > k:
            if nums[left] % 2 != 0:
                odd_count -= 1

            left += 1

        count += right - left + 1

    return count


def number_of_nice_subarrays(nums, k):
    if k <= 0:
        return 0

    return (
        at_most_k_odds(nums, k)
        - at_most_k_odds(nums, k - 1)
    )


print(number_of_nice_subarrays([1, 1, 2, 1, 1], 3))
print(number_of_nice_subarrays([2, 4, 6], 1))
print(number_of_nice_subarrays([1, 3, 5], 2))
print(number_of_nice_subarrays([2, 2, 2], 0))
