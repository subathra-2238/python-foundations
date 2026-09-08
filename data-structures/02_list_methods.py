# List Slicing and Methods

numbers = [10, 20, 30, 40, 50]

print("Original list:", numbers)

# Slicing
print("First three:", numbers[0:3])
print("Last two:", numbers[-2:])
print("Every second element:", numbers[::2])

# Useful methods
numbers.append(60)
print("\nAfter append:", numbers)

numbers.insert(1, 15)
print("After insert:", numbers)

numbers.remove(30)
print("After remove:", numbers)

numbers.sort()
print("After sort:", numbers)

numbers.reverse()
print("After reverse:", numbers)

print("Length:", len(numbers))