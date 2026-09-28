numbers = [10, 25, 7, 40, 15]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Smallest element:", smallest)