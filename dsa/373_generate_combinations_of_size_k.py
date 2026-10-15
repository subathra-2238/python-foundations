
numbers = [1, 2, 3, 4]
k = 2
combinations = []

def generate_combinations(start, current):
    if len(current) == k:
        combinations.append(current.copy())
        return

    for i in range(start, len(numbers)):
        current.append(numbers[i])
        generate_combinations(i + 1, current)
        current.pop()  # Backtrack

generate_combinations(0, [])

print("Numbers:", numbers)
print("Combination size:", k)
print("Combinations:")

for combination in combinations:
    print(combination)

print("Total combinations:", len(combinations))
