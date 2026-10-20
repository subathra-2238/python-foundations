def convert_to_title(column_number):
    result = ""

    while column_number > 0:
        column_number -= 1
        remainder = column_number % 26

        result = chr(ord("A") + remainder) + result
        column_number //= 26

    return result


print("Column title:", convert_to_title(1))
print("Column title:", convert_to_title(28))
print("Column title:", convert_to_title(701))
