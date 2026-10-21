def missing_number(nums):
    result = len(nums)

    for i, num in enumerate(nums):
        result ^= i ^ num

    return result


numbers = [3, 0, 1]
print("Missing number:", missing_number(numbers))

numbers = [0, 1]
print("Missing number:", missing_number(numbers))
