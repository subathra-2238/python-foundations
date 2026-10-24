def array_pair_sum(nums):
    nums.sort()
    total = 0

    for i in range(0, len(nums), 2):
        total += nums[i]

    return total


print(array_pair_sum([1, 4, 3, 2]))
print(array_pair_sum([6, 2, 6, 5, 1, 2]))
