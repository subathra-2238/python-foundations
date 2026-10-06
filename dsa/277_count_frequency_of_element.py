numbers = [10, 20, 10, 30, 20, 10, 40]
target = 20

count = 0

for number in numbers:
    if number == target:
        count += 1

print("Array:", numbers)
print("Target element:", target)
print("Frequency:", count)
