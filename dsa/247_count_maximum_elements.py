numbers = [25, 10, 45, 30, 45, 20, 45]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

count = 0

for number in numbers:
    if number == maximum:
        count += 1

print("Array:", numbers)
print("Maximum element:", maximum)
print("Count of maximum elements:", count)
