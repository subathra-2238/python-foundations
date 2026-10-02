numbers = [10, 25, 20, 30, 20]
value = 20

found = False

for number in numbers:
    if number == value:
        print("Array:", numbers)
        print("Given value:", value)
        print("First element equal to value:", number)
        found = True
        break

if not found:
    print("Value not found")
