numbers = [25, 10, 30, 15, 40, 50]

half = len(numbers) // 2

minimum = numbers[half]

for i in range(half, len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]

print("Array:", numbers)
print("Minimum element in second half:", minimum)
