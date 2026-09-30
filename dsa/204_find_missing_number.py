numbers = [1, 2, 3, 5, 6]

n = len(numbers) + 1
expected_sum = n * (n + 1) // 2

actual_sum = 0

for number in numbers:
    actual_sum += number

missing_number = expected_sum - actual_sum

print("Array:", numbers)
print("Missing number:", missing_number)