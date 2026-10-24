
def find_unsorted_subarray(nums):
    sorted_nums = sorted(nums)

    left = 0
    right = len(nums) - 1

    while left < len(nums) and nums[left] == sorted_nums[left]:
        left += 1

    if left == len(nums):
        return 0

    while nums[right] == sorted_nums[right]:
        right -= 1

    return right - left + 1


print(find_unsorted_subarray([2, 6, 4, 8, 10, 9, 15]))
print(find_unsorted_subarray([1, 2, 3, 4]))
print(find_unsorted_subarray([1, 3, 2, 2, 2]))
