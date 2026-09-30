numbers = [10, 20, 30, 40, 50]

first = numbers[0]

for i in range(len(numbers) - 1):
    numbers[i] = numbers[i + 1]

numbers[-1] = first

print("Original array: [10, 20, 30, 40, 50]")
print("Left rotated array:", numbers)