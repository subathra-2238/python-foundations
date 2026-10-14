numbers = [1, 2, 3]
subsets = []

def generate_subsets(index, current):
    if index == len(numbers):
        subsets.append(current.copy())
        return

    # Exclude the current element
    generate_subsets(index + 1, current)

    # Include the current element
    current.append(numbers[index])
    generate_subsets(index + 1, current)

    # Backtrack
    current.pop()

generate_subsets(0, [])

print("Array:", numbers)
print("All subsets:")

for subset in subsets:
    print(subset)

print("Total subsets:", len(subsets))
