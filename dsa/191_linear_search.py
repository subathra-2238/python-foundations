numbers = [10, 25, 7, 40, 15]
target = 40

index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        index = i
        break

print("Index:", index)