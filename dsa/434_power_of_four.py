def is_power_of_four(n):
    if n <= 0:
        return False

    while n % 4 == 0:
        n //= 4

    return n == 1


print("16:", is_power_of_four(16))
print("64:", is_power_of_four(64))
print("8:", is_power_of_four(8))
print("1:", is_power_of_four(1))
