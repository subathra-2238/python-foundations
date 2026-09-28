numbers = [-3, 0, 5, 0, 8, -1, 0, 4]

count = 0

for number in numbers:
    if number == 0:
        count += 1

print("Numbers:", numbers)
print("Number of zeroes:", count)