numbers = [10, 20, 10, 30, 20, 10, 40, 30]

elements = []

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    already_added = False

    for k in range(len(elements)):
        if elements[k] == numbers[i]:
            already_added = True
            break

    if count == 2 and not already_added:
        elements.append(numbers[i])

print("Array:", numbers)
print("Elements with frequency exactly two:", elements)