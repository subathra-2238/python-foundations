numbers = [10, 20, 15, 20, 30, 20]
value = 20

count = 0

for number in numbers:
    if number <= value:
        count += 1

print("Array:", numbers)
print("Given value:", value)
print("Count of elements less than or equal to value:", count)
