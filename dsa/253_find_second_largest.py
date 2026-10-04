numbers = [25, 10, 45, 30, 20]

largest = numbers[0]
second_largest = numbers[0]

for number in numbers:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        second_largest = number

print("Array:", numbers)
print("Largest element:", largest)
print("Second largest element:", second_largest)
