numbers = [1, 3, 5, 2, 4, 6, 8]

longest_length = 1
current_length = 1

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current_length += 1
    else:
        current_length = 1

    if current_length > longest_length:
        longest_length = current_length

print("Numbers:", numbers)
print("Length of longest strictly increasing run:", longest_length)