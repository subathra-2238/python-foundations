def count_even_digit_numbers(numbers):
    count = 0

    for number in numbers:
        digits = len(str(abs(number)))

        if digits % 2 == 0:
            count += 1

    return count


numbers = [12, 345, 2, 6, 7896, 1000]

print("Numbers:", numbers)
print("Count:", count_even_digit_numbers(numbers))
