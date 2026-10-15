
numbers = [1, 2, 3]
permutations = []

def generate_permutations(start):
    if start == len(numbers):
        permutations.append(numbers.copy())
        return

    for i in range(start, len(numbers)):
        # Choose an element
        numbers[start], numbers[i] = numbers[i], numbers[start]

        # Generate the remaining permutations
        generate_permutations(start + 1)

        # Backtrack: restore the original order
        numbers[start], numbers[i] = numbers[i], numbers[start]

generate_permutations(0)

print("Array:", numbers)
print("All permutations:")

for permutation in permutations:
    print(permutation)

print("Total permutations:", len(permutations))
