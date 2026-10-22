def integer_replacement(n):
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1

        steps += 1

    return steps


print("Steps for 8:", integer_replacement(8))
print("Steps for 7:", integer_replacement(7))
print("Steps for 15:", integer_replacement(15))
