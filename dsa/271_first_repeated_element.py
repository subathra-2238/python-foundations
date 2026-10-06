numbers = [10, 20, 30, 20, 40, 50]

repeated = None

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            repeated = numbers[i]
            break
    if repeated is not None:
        break

print("Array:", numbers)
print("First repeated element:", repeated)
