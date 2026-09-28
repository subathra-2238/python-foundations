# DSA-04: Linear Search

numbers = [10, 25, 37, 42, 56, 68]

target = 42

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")