numbers = [25, 10, 45, 10, 30, 20, 10]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

count = 0

for number in numbers:
    if number == minimum:
        count += 1

print("Array:", numbers)
print("Minimum element:", minimum)
print("Count of minimum elements:", count)
