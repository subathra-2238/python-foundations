numbers = [10, 20, 10, 30, 20, 10, 40, 30]

count_even_frequency = 0

for i in range(len(numbers)):
    count = 0

    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1

    already_counted = False

    for k in range(i):
        if numbers[k] == numbers[i]:
            already_counted = True
            break

    if count % 2 == 0 and not already_counted:
        count_even_frequency += 1

print("Array:", numbers)
print("Elements with even frequency:", count_even_frequency)
