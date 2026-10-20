def is_power_of_two(n):
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2

    return n == 1


print("8:", is_power_of_two(8))
print("6:", is_power_of_two(6))
print("1:", is_power_of_two(1))
print("0:", is_power_of_two(0))
