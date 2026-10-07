numbers = [10, 20, 10, 30, 20, 10, 40, 30]

least_frequent = numbers[0]
minimum_frequency = len(numbers) + 1

for number in numbers:
    count = 0

    for value in numbers:
        if number == value:
            count += 1

    if count < minimum_frequency:
        minimum_frequency = count
        least_frequent = number

print("Array:", numbers)
print("Least frequent element:", least_frequent)
print("Frequency:", minimum_frequency)