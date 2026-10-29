
def subset_sum(nums, target):
    result = []

    def backtrack(start, path, total):
        if total == target:
            result.append(path.copy())
            return

        if total > target:
            return

        for i in range(start, len(nums)):
            path.append(nums[i])

            backtrack(i + 1, path, total + nums[i])

            # Undo the choice
            path.pop()

    backtrack(0, [], 0)
    return result


print(subset_sum([2, 3, 5, 7], 10))
print(subset_sum([1, 2, 3, 4], 5))
print(subset_sum([4, 6], 3))
