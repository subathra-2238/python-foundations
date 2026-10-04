numbers = [25, 10, 30, 10, 45, 10]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

for i in range(len(numbers)):
    if numbers[i] == minimum:
        print("Array:", numbers)
        print("Minimum element:", minimum)
        print("First minimum element position:", i)
        break
