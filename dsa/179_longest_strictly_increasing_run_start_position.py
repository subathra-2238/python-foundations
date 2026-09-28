numbers = [1, 3, 5, 2, 4, 6, 8]

best_start = 0
best_length = 1
current_start = 0
current_length = 1

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current_length += 1
    else:
        if current_length > best_length:
            best_length = current_length
            best_start = current_start

        current_start = i
        current_length = 1

if current_length > best_length:
    best_length = current_length
    best_start = current_start

print("Numbers:", numbers)
print("Start position of longest strictly increasing run:", best_start + 1)