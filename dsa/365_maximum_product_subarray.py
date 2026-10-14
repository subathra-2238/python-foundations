numbers = [2, 3, -2, 4]

maximum_product = numbers[0]
current_max = numbers[0]
current_min = numbers[0]

for i in range(1, len(numbers)):
    number = numbers[i]

    if number < 0:
        current_max, current_min = current_min, current_max

    current_max = max(number, current_max * number)
    current_min = min(number, current_min * number)

    maximum_product = max(maximum_product, current_max)

print("Array:", numbers)
print("Maximum product of contiguous subarray:", maximum_product)
