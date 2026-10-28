
def palindrome_partitioning(s):
    result = []

    def backtrack(start, path):
        if start == len(s):
            result.append(path.copy())
            return

        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]

            # Continue only if the substring is a palindrome
            if substring != substring[::-1]:
                continue

            path.append(substring)
            backtrack(end, path)
            path.pop()

    backtrack(0, [])
    return result


print(palindrome_partitioning("aab"))
print(palindrome_partitioning("aba"))
print(palindrome_partitioning("abc"))
