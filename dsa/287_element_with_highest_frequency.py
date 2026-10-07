numbers = [10, 20, 10, 30, 20, 10, 40, 30]

highest_frequency = 0
highest_frequency_element = None

for number in numbers:
    count = 0

    for value in numbers:
        if number == value:
            count += 1

    if count > highest_frequency:
        highest_frequency = count
        highest_frequency_element = number

print("Array:", numbers)
print("Element with highest frequency:", highest_frequency_element)
print("Frequency:", highest_frequency)
