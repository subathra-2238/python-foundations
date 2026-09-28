numbers = [1, 2, 2, 3, 4, 4, 4, 5]

count = 0

for i in range(1, len(numbers)):
    if numbers[i] == numbers[i - 1]:
        count += 1

print("Numbers:", numbers)
print("Number of equal adjacent pairs:", count)