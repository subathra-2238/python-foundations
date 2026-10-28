
def subsets_with_duplicates(nums):
    nums.sort()
    result = []

    def backtrack(start, path):
        result.append(path.copy())

        for i in range(start, len(nums)):
            # Skip duplicate numbers at the same level
            if i > start and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result


print(subsets_with_duplicates([1, 2, 2]))
print(subsets_with_duplicates([0]))
print(subsets_with_duplicates([1, 2, 2, 3]))
