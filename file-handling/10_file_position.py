# File Position

with open("file-handling/sample.txt", "r") as file:
    print("Initial position:", file.tell())

    content = file.read(5)

    print("Content read:", content)
    print("Position after reading:", file.tell())

    file.seek(0)

    print("Position after seek:", file.tell())

    content = file.read(5)

    print("Content again:", content)