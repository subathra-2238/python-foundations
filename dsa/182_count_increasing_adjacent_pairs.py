numbers = [1, 3, 5, 2, 4, 6, 8]

count = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        count += 1

print("Numbers:", numbers)
print("Number of increasing adjacent pairs:", count)