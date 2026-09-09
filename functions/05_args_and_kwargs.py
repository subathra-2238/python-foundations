# *args and **kwargs

def add_numbers(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print("Sum 1:", add_numbers(10, 20))
print("Sum 2:", add_numbers(10, 20, 30, 40))


def student_info(**details):
    print("\nStudent Information")

    for key, value in details.items():
        print(key, ":", value)


student_info(
    name="Subathra",
    department="AI & ML",
    year=2
)