
def is_disarium(n):
    if n < 0:
        return False

    digits = str(n)

    def calculate_sum(index):
        if index == len(digits):
            return 0

        digit = int(digits[index])
        position = index + 1

        return digit ** position + calculate_sum(index + 1)

    return calculate_sum(0) == n


number = 135

print("Number:", number)

if is_disarium(number):
    print("It is a Disarium number.")
else:
    print("It is not a Disarium number.")
