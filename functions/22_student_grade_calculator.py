# Student Grade Calculator


def calculate_average(marks):
    return sum(marks) / len(marks)


def get_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


marks = []

for i in range(3):
    mark = float(input(f"Enter mark {i + 1}: "))
    marks.append(mark)


average = calculate_average(marks)
grade = get_grade(average)

print("\n--- Student Result ---")
print("Marks:", marks)
print("Average:", average)
print("Grade:", grade)