numbers = [25, 10, 45, 30, 20]

maximum = numbers[0]
minimum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

    if number < minimum:
        minimum = number

range_value = maximum - minimum

print("Array:", numbers)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
print("Range:", range_value)
