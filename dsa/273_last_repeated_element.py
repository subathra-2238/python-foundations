numbers = [10, 20, 30, 20, 40, 10, 50]

last_repeated = None

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            last_repeated = numbers[i]

print("Array:", numbers)
print("Last repeated element:", last_repeated)
