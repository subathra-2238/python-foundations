numbers = [10, 20, 10, 30, 20, 10, 40, 30]

element = None

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count == 3:
        element = numbers[i]

print("Array:", numbers)
print("Last element with frequency exactly three:", element)
