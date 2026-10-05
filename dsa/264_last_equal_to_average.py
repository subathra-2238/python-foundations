numbers = [10, 20, 30]

total = 0

for number in numbers:
    total += number

average = total / len(numbers)

print("Array:", numbers)
print("Average:", average)

found = False

for i in range(len(numbers) - 1, -1, -1):
    if numbers[i] == average:
        print("Last element equal to average:", numbers[i])
        found = True
        break

if not found:
    print("No element equal to average found")
