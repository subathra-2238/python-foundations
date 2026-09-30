numbers = [1, 5, 7, -1, 5]
target = 6

print("Array:", numbers)
print("Target sum:", target)
print("Pairs:")

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i], numbers[j])