numbers = [10, 3, 8, 15, 6]

minimum_difference = abs(numbers[0] - numbers[1])

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        difference = abs(numbers[i] - numbers[j])

        if difference < minimum_difference:
            minimum_difference = difference

print("Array:", numbers)
print("Minimum difference:", minimum_difference)