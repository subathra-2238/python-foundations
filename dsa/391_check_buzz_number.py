
def is_buzz_number(n):
    if n <= 0:
        return False

    return n % 7 == 0 or n % 10 == 7


number = 27

print("Number:", number)

if is_buzz_number(number):
    print("It is a Buzz number.")
else:
    print("It is not a Buzz number.")
