numbers = [10, 20, 10, 30, 10, 40]
target = 10

count = 0

for number in numbers:
    if number == target:
        count += 1

print("Occurrences:", count)