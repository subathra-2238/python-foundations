
# DSA 540: First Missing Positive

def first_missing_positive(nums):
    n = len(nums)

    # Place each number at its correct index
    for i in range(n):

        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:

            correct_index = nums[i] - 1

            nums[i], nums[correct_index] = nums[correct_index], nums[i]

    # Find the first number in the wrong position
    for i in range(n):

        if nums[i] != i + 1:
            return i + 1

    return n + 1


print(first_missing_positive([3, 4, -1, 1]))
print(first_missing_positive([1, 2, 0]))
print(first_missing_positive([7, 8, 9, 11, 12]))
print(first_missing_positive([1, 2, 3]))
