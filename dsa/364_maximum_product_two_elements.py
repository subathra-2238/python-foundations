numbers = [3, 5, 2, 8, 6]

largest = numbers[0]
second_largest = numbers[1]

if second_largest > largest:
    largest, second_largest = second_largest, largest

for number in numbers[2:]:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest:
        second_largest = number

product = largest * second_largest

print("Array:", numbers)
print("Largest element:", largest)
print("Second largest element:", second_largest)
print("Maximum product:", product)
