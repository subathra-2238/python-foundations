def is_self_dividing(number):
    original = number

    while number > 0:
        digit = number % 10

        if digit == 0 or original % digit != 0:
            return False

        number //= 10

    return True


def self_dividing_numbers(left, right):
    result = []

    for number in range(left, right + 1):
        if is_self_dividing(number):
            result.append(number)

    return result


print(self_dividing_numbers(1, 22))
print(self_dividing_numbers(20, 30))
