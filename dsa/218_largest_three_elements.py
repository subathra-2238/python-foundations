numbers = [10, 25, 7, 40, 15, 30]

largest = numbers[0]
second_largest = numbers[0]
third_largest = numbers[0]

for number in numbers:
    if number > largest:
        third_largest = second_largest
        second_largest = largest
        largest = number
    elif number > second_largest and number != largest:
        third_largest = second_largest
        second_largest = number
    elif number > third_largest and number != second_largest and number != largest:
        third_largest = number

print("Array:", numbers)
print("Largest three elements:", largest, second_largest, third_largest)