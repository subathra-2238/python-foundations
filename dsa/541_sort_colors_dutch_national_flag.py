
# DSA 541: Sort Colors
# Dutch National Flag Algorithm

def sort_colors(nums):
    low = 0
    mid = 0
    high = len(nums) - 1

    while mid <= high:

        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1

        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

    return nums


print(sort_colors([2, 0, 2, 1, 1, 0]))
print(sort_colors([2, 0, 1]))
print(sort_colors([0, 0, 1, 1, 2, 2]))
