numbers = [25, 10, 45, 30, 20]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

print("Array:", numbers)
print("Minimum element:", minimum)
