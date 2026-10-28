
def permute(nums):
    result = []

    def backtrack(path, remaining):
        if not remaining:
            result.append(path)
            return

        for i in range(len(remaining)):
            # Choose one number
            number = remaining[i]

            # Keep the chosen number and explore the rest
            backtrack(
                path + [number],
                remaining[:i] + remaining[i + 1:]
            )

    backtrack([], nums)
    return result


print(permute([1, 2]))
print(permute([1, 2, 3]))
print(permute([5]))
