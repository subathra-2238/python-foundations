numbers = [-10, 15, -20, 25, 30, -35]

count = 0

for number in numbers:
    if number < 0:
        count += 1

print("Array:", numbers)
print("Number of negative elements:", count)
