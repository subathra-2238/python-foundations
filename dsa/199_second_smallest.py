numbers = [10, 25, 7, 40, 15]

smallest = numbers[0]
second_smallest = numbers[0]

for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif number < second_smallest and number != smallest:
        second_smallest = number

print("Second smallest:", second_smallest)