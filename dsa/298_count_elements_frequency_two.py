numbers = [10, 20, 10, 30, 20, 10, 40, 30]

count_frequency_two = 0

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    if count == 2:
        already_counted = False

        for k in range(i):
            if numbers[k] == numbers[i]:
                already_counted = True
                break

        if not already_counted:
            count_frequency_two += 1

print("Array:", numbers)
print("Elements with frequency exactly two:", count_frequency_two)