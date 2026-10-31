
# DSA 537: Maximum Product of Three Numbers

def maximum_product(nums):
    nums.sort()

    n = len(nums)

    # Option 1: Three largest numbers
    product1 = nums[n - 1] * nums[n - 2] * nums[n - 3]

    # Option 2: Two smallest and one largest
    product2 = nums[0] * nums[1] * nums[n - 1]

    return max(product1, product2)


print(maximum_product([1, 2, 3, 4]))
print(maximum_product([-10, -10, 5, 2]))
print(maximum_product([-1, -2, -3, -4]))
