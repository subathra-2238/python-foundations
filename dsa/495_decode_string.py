
def decode_string(s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)

        elif char == "[":
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0

        elif char == "]":
            previous_string, repeat_count = stack.pop()
            current_string = (
                previous_string + current_string * repeat_count
            )

        else:
            current_string += char

    return current_string


print(decode_string("3[a]"))
print(decode_string("3[a2[c]]"))
print(decode_string("2[abc]3[cd]ef"))
print(decode_string("10[x]"))
