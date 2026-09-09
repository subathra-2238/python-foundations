# Variable Scope

name = "Subathra"


def show_name():
    print("Inside function:", name)


show_name()

print("Outside function:", name)


def change_name():
    name = "Sivasri"
    print("Inside function:", name)


change_name()

print("Outside function:", name)