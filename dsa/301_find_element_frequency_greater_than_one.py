numbers = [10, 20, 10, 30, 20, 10, 40, 30]

element = None

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count > 1:
        element = numbers[i]
        break

print("Array:", numbers)
print("First element with frequency greater than one:", element)
