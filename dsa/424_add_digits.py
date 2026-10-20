def add_digits(num):
    while num >= 10:
        total = 0

        while num > 0:
            total += num % 10
            num //= 10

        num = total

    return num


print("Result:", add_digits(9875))
print("Result:", add_digits(38))
print("Result:", add_digits(9))
