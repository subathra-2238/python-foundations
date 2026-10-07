numbers = [10, 20, 10, 30, 20, 10, 40, 30]

lowest_frequency = len(numbers) + 1
lowest_frequency_element = None

for number in numbers:
    count = 0

    for value in numbers:
        if number == value:
            count += 1

    if count < lowest_frequency:
        lowest_frequency = count
        lowest_frequency_element = number

print("Array:", numbers)
print("Element with lowest frequency:", lowest_frequency_element)
print("Frequency:", lowest_frequency)
