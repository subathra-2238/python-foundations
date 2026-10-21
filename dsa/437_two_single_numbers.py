def two_single_numbers(nums):
    xor_total = 0

    for num in nums:
        xor_total ^= num

    # Find the rightmost set bit.
    rightmost_bit = xor_total & -xor_total

    first = 0
    second = 0

    for num in nums:
        if num & rightmost_bit:
            first ^= num
        else:
            second ^= num

    return first, second


numbers = [1, 2, 1, 3, 2, 5]
first, second = two_single_numbers(numbers)

print("Single numbers:", sorted([first, second]))
