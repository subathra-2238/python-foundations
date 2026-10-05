numbers = [25, 10, 30, 15, 40, 50]

half = len(numbers) // 2

minimum = numbers[0]

for i in range(half):
    if numbers[i] < minimum:
        minimum = numbers[i]

print("Array:", numbers)
print("Minimum element in first half:", minimum)
