numbers1 = [10, 20, 30, 40, 50]
numbers2 = [20, 40, 60, 80]

common_elements = []

for number in numbers1:
    if number in numbers2 and number not in common_elements:
        common_elements.append(number)

print("First array:", numbers1)
print("Second array:", numbers2)
print("Common elements:", common_elements)