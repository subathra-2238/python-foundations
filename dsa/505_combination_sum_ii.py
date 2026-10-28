
def combination_sum_ii(candidates, target):
    candidates.sort()
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path.copy())
            return

        for i in range(start, len(candidates)):
            # Skip duplicates at the same level
            if i > start and candidates[i] == candidates[i - 1]:
                continue

            if candidates[i] > remaining:
                break

            path.append(candidates[i])

            # i + 1 means each element is used only once
            backtrack(i + 1, path, remaining - candidates[i])

            path.pop()

    backtrack(0, [], target)
    return result


print(combination_sum_ii([10, 1, 2, 7, 6, 1, 5], 8))
print(combination_sum_ii([2, 5, 2, 1, 2], 5))
print(combination_sum_ii([3, 4], 2))
