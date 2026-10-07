numbers = [10, 20, 10, 30, 20, 10, 40, 30]

elements = []

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count == 1:
        elements.append(numbers[i])

print("Array:", numbers)
print("Elements with frequency exactly one:", elements)