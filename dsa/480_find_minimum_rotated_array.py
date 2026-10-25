
def find_minimum(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]


print(find_minimum([3, 4, 5, 1, 2]))
print(find_minimum([4, 5, 6, 7, 0, 1, 2]))
print(find_minimum([11, 13, 15, 17]))
