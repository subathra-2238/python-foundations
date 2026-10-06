numbers = [10, 20, 10, 30, 20, 10, 40, 30]

highest_frequency = 0
second_highest_frequency = 0
most_frequent = None
second_most_frequent = None

for number in numbers:
    count = 0

    for value in numbers:
        if number == value:
            count += 1

    if count > highest_frequency:
        second_highest_frequency = highest_frequency
        second_most_frequent = most_frequent

        highest_frequency = count
        most_frequent = number

    elif count > second_highest_frequency and count < highest_frequency:
        second_highest_frequency = count
        second_most_frequent = number

print("Array:", numbers)
print("Second most frequent element:", second_most_frequent)
print("Frequency:", second_highest_frequency)
