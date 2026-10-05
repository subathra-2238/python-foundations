numbers = [10, 25, 15, 40, 30, 50]

half = len(numbers) // 2

maximum = numbers[0]

for i in range(half):
    if numbers[i] > maximum:
        maximum = numbers[i]

count = 0

for i in range(half, len(numbers)):
    if numbers[i] > maximum:
        count += 1

print("Array:", numbers)
print("Maximum of first half:", maximum)
print("Count of elements in second half greater than first-half maximum:", count)
