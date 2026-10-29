
def target_sum(nums, target):
    # dp[total] = number of ways to make total
    dp = {0: 1}

    for num in nums:
        next_dp = {}

        for total, ways in dp.items():
            plus_total = total + num
            minus_total = total - num

            next_dp[plus_total] = (
                next_dp.get(plus_total, 0) + ways
            )
            next_dp[minus_total] = (
                next_dp.get(minus_total, 0) + ways
            )

        dp = next_dp

    return dp.get(target, 0)


print(target_sum([1, 1, 1, 1, 1], 3))
print(target_sum([1], 1))
print(target_sum([1, 2, 3], 7))
