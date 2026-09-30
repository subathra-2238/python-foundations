numbers1 = [10, 20, 30, 40]
numbers2 = [30, 40, 50, 60]

union = []

for number in numbers1:
    if number not in union:
        union.append(number)

for number in numbers2:
    if number not in union:
        union.append(number)

print("First array:", numbers1)
print("Second array:", numbers2)
print("Union:", union)