def trailing_zeros(n):
    count = 0

    while n >= 5:
        n //= 5
        count += n

    return count


print("10!:", trailing_zeros(10))
print("25!:", trailing_zeros(25))
print("100!:", trailing_zeros(100))
