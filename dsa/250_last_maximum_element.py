numbers = [25, 45, 10, 45, 30, 45]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] == maximum:
        print("Array:", numbers)
        print("Maximum element:", maximum)
        print("Last maximum element position:", i)
        break
