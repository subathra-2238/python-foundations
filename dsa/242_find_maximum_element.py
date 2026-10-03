numbers = [25, 10, 45, 30, 20]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

print("Array:", numbers)
print("Maximum element:", maximum)
