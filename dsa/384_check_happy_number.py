
def sum_of_squares(n):
    if n == 0:
        return 0

    digit = n % 10
    return digit * digit + sum_of_squares(n // 10)


def is_happy(n, seen=None):
    if n <= 0:
        return False

    if seen is None:
        seen = set()

    if n == 1:
        return True

    if n in seen:
        return False

    seen.add(n)
    return is_happy(sum_of_squares(n), seen)


number = 19

print("Number:", number)

if is_happy(number):
    print("It is a Happy number.")
else:
    print("It is not a Happy number.")
