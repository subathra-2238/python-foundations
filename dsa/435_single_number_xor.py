def single_number(nums):
    result = 0

    for num in nums:
        result ^= num

    return result


print("Single number:", single_number([4, 1, 2, 1, 2]))
print("Single number:", single_number([7, 3, 7, 5, 5]))
