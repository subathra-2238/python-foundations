numbers = [25, 45, 10, 45, 30, 45]

maximum = numbers[0]

for number in numbers:
    if number > maximum:
        maximum = number

for i in range(len(numbers)):
    if numbers[i] == maximum:
        print("Array:", numbers)
        print("Maximum element:", maximum)
        print("First maximum element position:", i)
        break
