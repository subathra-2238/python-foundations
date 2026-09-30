numbers = [10, 20, 30, 40, 50]

last = numbers[-1]

for i in range(len(numbers) - 1, 0, -1):
    numbers[i] = numbers[i - 1]

numbers[0] = last

print("Original array: [10, 20, 30, 40, 50]")
print("Right rotated array:", numbers)
