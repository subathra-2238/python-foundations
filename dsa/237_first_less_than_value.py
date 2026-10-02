numbers = [30, 25, 20, 15, 10]
value = 18

found = False

for number in numbers:
    if number < value:
        print("Array:", numbers)
        print("Given value:", value)
        print("First element less than value:", number)
        found = True
        break

if not found:
    print("No element less than value found")
