numbers = [25, 10, 30, 10, 45, 10]

minimum = numbers[0]

for number in numbers:
    if number < minimum:
        minimum = number

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] == minimum:
        print("Array:", numbers)
        print("Minimum element:", minimum)
        print("Last minimum element position:", i)
        break
