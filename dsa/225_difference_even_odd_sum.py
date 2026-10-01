numbers = [10, 15, 20, 25, 30, 35]

even_sum = 0
odd_sum = 0

for number in numbers:
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

difference = abs(even_sum - odd_sum)

print("Array:", numbers)
print("Sum of even elements:", even_sum)
print("Sum of odd elements:", odd_sum)
print("Difference:", difference)
