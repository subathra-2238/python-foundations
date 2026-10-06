numbers = [10, 20, 10, 30, 20, 10, 40, 30]

lowest_frequency = len(numbers) + 1
second_lowest_frequency = len(numbers) + 1

least_frequent = None
second_least_frequent = None

for number in numbers:
    count = 0

    for value in numbers:
        if number == value:
            count += 1

    if count < lowest_frequency:
        second_lowest_frequency = lowest_frequency
        second_least_frequent = least_frequent

        lowest_frequency = count
        least_frequent = number

    elif count < second_lowest_frequency and count > lowest_frequency:
        second_lowest_frequency = count
        second_least_frequent = number

print("Array:", numbers)
print("Second least frequent element:", second_least_frequent)
print("Frequency:", second_lowest_frequency)
