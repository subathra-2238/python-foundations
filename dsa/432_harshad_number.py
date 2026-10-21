def is_harshad(n):
    if n <= 0:
        return False

    digit_sum = 0
    temp = n

    while temp > 0:
        digit_sum += temp % 10
        temp //= 10

    return n % digit_sum == 0


print("18:", is_harshad(18))
print("19:", is_harshad(19))
print("21:", is_harshad(21))
print("0:", is_harshad(0))
