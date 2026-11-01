
# DSA 543: Longest Consecutive Sequence

def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0

    for num in num_set:

        # Start only from the beginning of a sequence
        if num - 1 not in num_set:

            current_num = num
            current_length = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1

            longest = max(longest, current_length)

    return longest


print(longest_consecutive([100, 4, 200, 1, 3, 2]))
print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 1]))
print(longest_consecutive([1, 2, 0, 1]))
print(longest_consecutive([]))
