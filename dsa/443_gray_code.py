def gray_code(n):
    result = []

    for i in range(1 << n):
        result.append(i ^ (i >> 1))

    return result


print("Gray code (n=2):", gray_code(2))
print("Gray code (n=3):", gray_code(3))
