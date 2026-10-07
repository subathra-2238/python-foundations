numbers = [10, 20, 10, 30, 20, 40, 50]

duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])

print("Array:", numbers)
print("Duplicate elements:", duplicates)
