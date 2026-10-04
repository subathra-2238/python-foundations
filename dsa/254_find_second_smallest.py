numbers = [25, 10, 45, 30, 20]

smallest = numbers[0]
second_smallest = numbers[0]

for number in numbers:
    if number < smallest:
        second_smallest = smallest
        smallest = number
    elif number < second_smallest and number != smallest:
        second_smallest = number

print("Array:", numbers)
print("Smallest element:", smallest)
print("Second smallest element:", second_smallest)
