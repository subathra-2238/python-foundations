
def split_array(nums, k):
    left = max(nums)
    right = sum(nums)

    while left < right:
        mid = (left + right) // 2

        subarrays = 1
        current_sum = 0

        for num in nums:
            if current_sum + num > mid:
                subarrays += 1
                current_sum = num
            else:
                current_sum += num

        if subarrays <= k:
            right = mid
        else:
            left = mid + 1

    return left


print(split_array([7, 2, 5, 10, 8], 2))
print(split_array([1, 2, 3, 4, 5], 2))
print(split_array([1, 4, 4], 3))
print(split_array([5, 5, 5, 5], 2))
