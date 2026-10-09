numbers = [10, 20, 10, 30, 20, 10, 40]

maximum_frequency = 0

for number in numbers:
    count = 0

    for value in numbers:
        if number == value:
            count += 1

    if count > maximum_frequency:
        maximum_frequency = count

print("Array:", numbers)
print("Maximum frequency:", maximum_frequency)
