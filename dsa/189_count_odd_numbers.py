numbers = [3, 8, 12, 5, 7, 10, 14]

count = 0

for number in numbers:
    if number % 2 != 0:
        count += 1

print("Numbers:", numbers)
print("Number of odd numbers:", count)