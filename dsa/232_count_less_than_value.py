numbers = [10, 25, 15, 40, 30, 5]
value = 20

count = 0

for number in numbers:
    if number < value:
        count += 1

print("Array:", numbers)
print("Given value:", value)
print("Count of elements less than value:", count)
