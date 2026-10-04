numbers = [25, 10, 45, 30, 20]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

difference = largest - smallest

print("Array:", numbers)
print("Largest element:", largest)
print("Smallest element:", smallest)
print("Difference:", difference)
