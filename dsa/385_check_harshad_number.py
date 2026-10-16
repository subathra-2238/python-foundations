
def sum_of_digits(n):
    if n == 0:
        return 0

    return n % 10 + sum_of_digits(n // 10)


def is_harshad(n):
    if n <= 0:
        return False

    digit_sum = sum_of_digits(n)
    return n % digit_sum == 0


number = 18

print("Number:", number)
print("Sum of digits:", sum_of_digits(number))

if is_harshad(number):
    print("It is a Harshad number.")
else:
    print("It is not a Harshad number.")
