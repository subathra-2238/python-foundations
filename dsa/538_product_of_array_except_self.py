
# DSA 538: Product of Array Except Self

def product_except_self(nums):
    n = len(nums)

    result = [1] * n

    # Calculate prefix products
    prefix = 1

    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    # Calculate suffix products
    suffix = 1

    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]

    return result


print(product_except_self([1, 2, 3, 4]))
print(product_except_self([-1, 1, 0, -3, 3]))
print(product_except_self([2, 3, 4, 5]))
