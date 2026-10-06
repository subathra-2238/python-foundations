numbers = [10, 20, 30, 20, 40, 10, 50]

last_non_repeated = None

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count == 1:
        last_non_repeated = numbers[i]

print("Array:", numbers)
print("Last non-repeated element:", last_non_repeated)
