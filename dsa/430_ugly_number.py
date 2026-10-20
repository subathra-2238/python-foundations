def is_ugly(n):
    if n <= 0:
        return False

    for factor in [2, 3, 5]:
        while n % factor == 0:
            n //= factor

    return n == 1


print("6:", is_ugly(6))
print("14:", is_ugly(14))
print("1:", is_ugly(1))
print("30:", is_ugly(30))
