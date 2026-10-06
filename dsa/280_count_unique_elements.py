numbers = [10, 20, 10, 30, 20, 40, 50]

unique_count = 0

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count == 1:
        unique_count += 1

print("Array:", numbers)
print("Number of unique elements:", unique_count)
