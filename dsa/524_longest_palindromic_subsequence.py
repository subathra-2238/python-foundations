
def longest_palindromic_subsequence(s):
    n = len(s)

    if n == 0:
        return 0

    # dp[i][j] = LPS length between indices i and j
    dp = [[0] * n for _ in range(n)]

    # Every single character is a palindrome
    for i in range(n):
        dp[i][i] = 1

    # Check substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(
                    dp[i + 1][j],
                    dp[i][j - 1]
                )

    return dp[0][n - 1]


print(longest_palindromic_subsequence("bbbab"))
print(longest_palindromic_subsequence("cbbd"))
print(longest_palindromic_subsequence("racecar"))
print(longest_palindromic_subsequence(""))
