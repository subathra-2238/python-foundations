numbers = [30, 25, 15, 40, 10]
value = 20

found = False

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] < value:
        print("Array:", numbers)
        print("Given value:", value)
        print("Last element less than value:", numbers[i])
        found = True
        break

if not found:
    print("No element less than value found")
