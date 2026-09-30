numbers = [1, 2, 3, 4, 5, 6]
target = 9

print("Array:", numbers)
print("Target sum:", target)
print("Triplets:")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        for k in range(j + 1, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == target:
                print(numbers[i], numbers[j], numbers[k])