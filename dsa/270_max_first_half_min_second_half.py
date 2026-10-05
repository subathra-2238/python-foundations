numbers = [25, 10, 30, 15, 40, 50]

half = len(numbers) // 2

maximum = numbers[0]

for i in range(half):
    if numbers[i] > maximum:
        maximum = numbers[i]

minimum = numbers[half]

for i in range(half, len(numbers)):
    if numbers[i] < minimum:
        minimum = numbers[i]

print("Array:", numbers)
print("Maximum element in first half:", maximum)
print("Minimum element in second half:", minimum)
