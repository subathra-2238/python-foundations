
def min_remove_to_make_valid(s):
    result = []
    stack = []

    for char in s:
        if char == "(":
            stack.append(len(result))
            result.append(char)

        elif char == ")":
            if stack:
                stack.pop()
                result.append(char)
            # Ignore unmatched closing parentheses

        else:
            result.append(char)

    # Remove unmatched opening parentheses
    for index in stack:
        result[index] = ""

    return "".join(result)


print(min_remove_to_make_valid("lee(t(c)o)de)"))
print(min_remove_to_make_valid("a)b(c)d"))
print(min_remove_to_make_valid("))(("))
print(min_remove_to_make_valid("(a(b)c)"))
