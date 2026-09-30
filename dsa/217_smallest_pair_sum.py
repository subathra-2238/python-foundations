numbers = [10, 25, 7, 40, 15]

smallest_sum = numbers[0] + numbers[1]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        pair_sum = numbers[i] + numbers[j]

        if pair_sum < smallest_sum:
            smallest_sum = pair_sum

print("Array:", numbers)
print("Smallest pair sum:", smallest_sum)