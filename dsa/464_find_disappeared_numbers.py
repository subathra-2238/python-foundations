def find_disappeared_numbers(nums):
    n = len(nums)
    present = set(nums)
    missing = []

    for number in range(1, n + 1):
        if number not in present:
            missing.append(number)

    return missing


print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(find_disappeared_numbers([1, 1]))
print(find_disappeared_numbers([1, 2, 3]))
