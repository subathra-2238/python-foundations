numbers1 = [10, 20, 30, 40, 50]
numbers2 = [20, 40, 60, 80]

intersection = []

for number in numbers1:
    if number in numbers2 and number not in intersection:
        intersection.append(number)

print("First array:", numbers1)
print("Second array:", numbers2)
print("Intersection:", intersection)