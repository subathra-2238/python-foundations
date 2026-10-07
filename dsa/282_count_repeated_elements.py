numbers = [10, 20, 10, 30, 20, 40, 50]

repeated_count = 0

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count > 1:
        already_counted = False

        for k in range(i):
            if numbers[k] == numbers[i]:
                already_counted = True
                break

        if not already_counted:
            repeated_count += 1

print("Array:", numbers)
print("Number of repeated elements:", repeated_count)
