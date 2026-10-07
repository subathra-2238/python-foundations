numbers = [10, 20, 10, 30, 20, 10, 40, 30]

most_frequent = numbers[0]
maximum_frequency = 0

for number in numbers:
    count = 0

    for value in numbers:
        if number == value:
            count += 1

    if count > maximum_frequency:
        maximum_frequency = count
        most_frequent = number

print("Array:", numbers)
print("Most frequent element:", most_frequent)
print("Frequency:", maximum_frequency)