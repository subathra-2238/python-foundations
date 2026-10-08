numbers = [10, 20, 10, 30, 20, 10, 40, 30]

maximum_frequency = 0
minimum_frequency = len(numbers) + 1

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count > maximum_frequency:
        maximum_frequency = count

    if count < minimum_frequency:
        minimum_frequency = count

difference = maximum_frequency - minimum_frequency

print("Array:", numbers)
print("Maximum frequency:", maximum_frequency)
print("Minimum frequency:", minimum_frequency)
print("Frequency difference:", difference)
