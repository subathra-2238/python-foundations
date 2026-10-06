numbers = [10, 20, 30, 20, 40, 10]

first_non_repeated = None

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count == 1:
        first_non_repeated = numbers[i]
        break

print("Array:", numbers)
print("First non-repeated element:", first_non_repeated)
