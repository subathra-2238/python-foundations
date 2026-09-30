numbers = [10, 25, 7, 40, 15]

pair_sums = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        pair_sum = numbers[i] + numbers[j]
        pair_sums.append(pair_sum)

largest_sum = pair_sums[0]
second_largest_sum = pair_sums[0]

for pair_sum in pair_sums:
    if pair_sum > largest_sum:
        second_largest_sum = largest_sum
        largest_sum = pair_sum
    elif pair_sum > second_largest_sum and pair_sum != largest_sum:
        second_largest_sum = pair_sum

print("Array:", numbers)
print("Largest pair sum:", largest_sum)
print("Second largest pair sum:", second_largest_sum)