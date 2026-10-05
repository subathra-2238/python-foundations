numbers = [25, 10, 30, 15, 40, 50]

half = len(numbers) // 2

maximum = numbers[half]

for i in range(half, len(numbers)):
    if numbers[i] > maximum:
        maximum = numbers[i]

print("Array:", numbers)
print("Maximum element in second half:", maximum)
