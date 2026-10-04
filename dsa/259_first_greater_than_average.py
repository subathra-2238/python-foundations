numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

average = total / len(numbers)

found = False

for number in numbers:
    if number > average:
        print("Array:", numbers)
        print("Average:", average)
        print("First element greater than average:", number)
        found = True
        break

if not found:
    print("No element greater than average found")
