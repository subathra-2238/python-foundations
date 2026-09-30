numbers = [10, 25, 7, 40, 15, 30]

smallest = numbers[0]
second_smallest = numbers[0]
third_smallest = numbers[0]

for number in numbers:
    if number < smallest:
        third_smallest = second_smallest
        second_smallest = smallest
        smallest = number
    elif number < second_smallest and number != smallest:
        third_smallest = second_smallest
        second_smallest = number
    elif number < third_smallest and number != second_smallest and number != smallest:
        third_smallest = number

print("Array:", numbers)
print("Smallest three elements:", smallest, second_smallest, third_smallest)