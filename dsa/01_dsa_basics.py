# DSA-01: DSA Basics

marks = [85, 92, 76, 90, 88]

highest = marks[0]

for mark in marks:
    if mark > highest:
        highest = mark

print("Marks:", marks)
print("Highest mark:", highest)