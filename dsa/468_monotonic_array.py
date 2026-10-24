def is_monotonic(nums):
    increasing = True
    decreasing = True

    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            increasing = False

        if nums[i] > nums[i - 1]:
            decreasing = False

    return increasing or decreasing


print(is_monotonic([1, 2, 2, 3]))
print(is_monotonic([6, 5, 4, 4]))
print(is_monotonic([1, 3, 2]))
print(is_monotonic([5, 5, 5]))
