numbers = [10, 25, 15, 40, 30, 50]

half = len(numbers) // 2

maximum = numbers[0]

for i in range(half):
    if numbers[i] > maximum:
        maximum = numbers[i]

print("Array:", numbers)
print("Maximum element in first half:", maximum)
