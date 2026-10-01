 numbers = [10, 15, 20, 25, 30, 35]

total = 0

for number in numbers:
    if number % 2 == 0:
        total += number

print("Array:", numbers)
print("Sum of even elements:", total)
