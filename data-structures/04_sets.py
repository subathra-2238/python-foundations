# Python Sets

numbers = {10, 20, 30, 20, 40, 10}

print("Set:", numbers)

# Adding an element
numbers.add(50)
print("After adding 50:", numbers)

# Removing an element
numbers.remove(30)
print("After removing 30:", numbers)

# Checking membership
print("Is 20 present?", 20 in numbers)
print("Is 100 present?", 100 in numbers)

# Length
print("Number of unique values:", len(numbers))