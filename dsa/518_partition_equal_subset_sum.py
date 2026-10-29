
def can_partition(nums):
    total = sum(nums)

    # An odd total cannot be split equally
    if total % 2 != 0:
        return False

    target = total // 2

    # dp[s] tells us whether sum s is achievable
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        for s in range(target, num - 1, -1):
            dp[s] = dp[s] or dp[s - num]

    return dp[target]


print(can_partition([1, 5, 11, 5]))
print(can_partition([1, 2, 3, 5]))
print(can_partition([2, 2, 3, 5]))
