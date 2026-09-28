numbers = [10, 20, 30, 40, 50]

is_sorted = True

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break

if is_sorted:
    print("Array is sorted")
else:
    print("Array is not sorted")