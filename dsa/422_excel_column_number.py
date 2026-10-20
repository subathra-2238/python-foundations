def title_to_number(column_title):
    result = 0

    for char in column_title:
        result = result * 26 + (ord(char) - ord("A") + 1)

    return result


print("Column number:", title_to_number("A"))
print("Column number:", title_to_number("AB"))
print("Column number:", title_to_number("ZY"))
