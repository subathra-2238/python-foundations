numbers = [10, 0, 20, 0, 30, 40, 0]

count = 0

for number in numbers:
    if number == 0:
        count += 1

print("Array:", numbers)
print("Number of zero elements:", count)
