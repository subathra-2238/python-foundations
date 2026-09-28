def longest_strictly_decreasing_run_end_position(numbers):
    if not numbers:
        return None

    longest_length = 1
    current_length = 1
    longest_end_position = 1

    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i - 1]:
            current_length += 1
        else:
            current_length = 1

        if current_length > longest_length:
            longest_length = current_length
            longest_end_position = i + 1

    return longest_end_position


numbers = [6, 5, 4, 7, 6, 5, 4]

result = longest_strictly_decreasing_run_end_position(numbers)

print("Numbers:", numbers)
print("End position of longest strictly decreasing run:", result)