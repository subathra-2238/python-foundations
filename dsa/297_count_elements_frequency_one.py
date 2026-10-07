numbers = [10, 20, 10, 30, 20, 10, 40, 30]

count_frequency_one = 0

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count == 1:
        count_frequency_one += 1

print("Array:", numbers)
print("Elements with frequency exactly one:", count_frequency_one)