
def digit_sum(n):
    total = 0

    while n > 0:
        total += n % 10
        n //= 10

    return total


def is_smith_number(n):
    if n < 4:
        return False

    original_sum = digit_sum(n)
    remaining = n
    factor_sum = 0
    divisor = 2

    while divisor * divisor <= remaining:
        while remaining % divisor == 0:
            factor_sum += digit_sum(divisor)
            remaining //= divisor
        divisor += 1

    if remaining > 1:
        factor_sum += digit_sum(remaining)

    return remaining != n and original_sum == factor_sum


number = 666

print("Number:", number)

if is_smith_number(number):
    print("It is a Smith number.")
else:
    print("It is not a Smith number.")
