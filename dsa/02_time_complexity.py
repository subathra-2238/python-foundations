# DSA-02: Time Complexity

numbers = [10, 20, 30, 40, 50]

# O(1) - Constant Time
print("First number:", numbers[0])


# O(n) - Linear Time
print("All numbers:")

for number in numbers:
    print(number)


# O(n²) - Quadratic Time
print("All pairs:")

for number1 in numbers:
    for number2 in numbers:
        print(number1, number2)