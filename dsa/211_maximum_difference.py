numbers = [7, 1, 5, 3, 6, 4]

minimum = numbers[0]
maximum_difference = 0

for i in range(1, len(numbers)):
    difference = numbers[i] - minimum

    if difference > maximum_difference:
        maximum_difference = difference

    if numbers[i] < minimum:
        minimum = numbers[i]

print("Array:", numbers)
print("Maximum difference:", maximum_difference)