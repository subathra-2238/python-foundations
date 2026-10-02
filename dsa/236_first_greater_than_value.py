numbers = [10, 15, 25, 30, 40]
value = 20

found = False

for number in numbers:
    if number > value:
        print("Array:", numbers)
        print("Given value:", value)
        print("First element greater than value:", number)
        found = True
        break

if not found:
    print("No element greater than value found")
