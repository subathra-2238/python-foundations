numbers = [10, 20, 30, 20, 40, 20]
value = 20

found = False

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] == value:
        print("Array:", numbers)
        print("Given value:", value)
        print("Last element equal to value:", numbers[i])
        found = True
        break

if not found:
    print("Value not found")
