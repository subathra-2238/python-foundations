numbers = [10, 25, 15, 40, 30]
value = 20

found = False

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] > value:
        print("Array:", numbers)
        print("Given value:", value)
        print("Last element greater than value:", numbers[i])
        found = True
        break

if not found:
    print("No element greater than value found")
