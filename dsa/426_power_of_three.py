def is_power_of_three(n):
    if n <= 0:
        return False

    while n % 3 == 0:
        n //= 3

    return n == 1


print("27:", is_power_of_three(27))
print("12:", is_power_of_three(12))
print("1:", is_power_of_three(1))
print("0:", is_power_of_three(0))
