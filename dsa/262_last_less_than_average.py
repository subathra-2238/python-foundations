numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

average = total / len(numbers)

found = False

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] < average:
        print("Array:", numbers)
        print("Average:", average)
        print("Last element less than average:", numbers[i])
        found = True
        break

if not found:
    print("No element less than average found")
