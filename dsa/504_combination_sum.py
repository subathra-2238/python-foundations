
def combination_sum(candidates, target):
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path.copy())
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            number = candidates[i]

            path.append(number)

            # Use i again because a number can be reused
            backtrack(i, path, remaining - number)

            # Undo the choice before trying another number
            path.pop()

    backtrack(0, [], target)
    return result


print(combination_sum([2, 3, 6, 7], 7))
print(combination_sum([2, 3, 5], 8))
print(combination_sum([2], 1))
