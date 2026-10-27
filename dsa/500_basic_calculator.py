
def calculate(s):
    result = 0
    number = 0
    sign = 1
    stack = []

    for char in s:
        if char.isdigit():
            number = number * 10 + int(char)

        elif char == "+":
            result += sign * number
            number = 0
            sign = 1

        elif char == "-":
            result += sign * number
            number = 0
            sign = -1

        elif char == "(":
            stack.append(result)
            stack.append(sign)
            result = 0
            sign = 1

        elif char == ")":
            result += sign * number
            number = 0

            result *= stack.pop()  # Sign before "("
            result += stack.pop()  # Result before "("

    return result + sign * number


print(calculate("1 + 1"))
print(calculate(" 2-1 + 2 "))
print(calculate("(1 + (4 + 5 + 2) - 3) + (6 + 8)"))
print(calculate("-(3 + 2)"))
