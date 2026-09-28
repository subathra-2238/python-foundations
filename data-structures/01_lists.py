# Python Lists

fruits = ["apple", "banana", "mango", "orange"]

print("Fruits:", fruits)

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Adding an element
fruits.append("grapes")
print("\nAfter adding grapes:", fruits)

# Updating an element
fruits[1] = "watermelon"
print("After updating:", fruits)

# Removing an element
fruits.remove("orange")
print("After removing orange:", fruits)

# List length
print("Number of fruits:", len(fruits))

# Loop through a list
print("\nAll fruits:")

for fruit in fruits:
    print(fruit)