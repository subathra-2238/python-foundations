
def calculate(s):
    stack = []
    number = 0
    operator = "+"

    for i, char in enumerate(s):
        if char.isdigit():
            number = number * 10 + int(char)

        if char in "+-*/" or i == len(s) - 1:
            if operator == "+":
                stack.append(number)
            elif operator == "-":
                stack.append(-number)
            elif operator == "*":
                stack.append(stack.pop() * number)
            elif operator == "/":
                previous = stack.pop()
                stack.append(int(previous / number))

            operator = char
            number = 0

    return sum(stack)


print(calculate("3+2*2"))
print(calculate(" 3/2 "))
print(calculate(" 3+5 / 2 "))
print(calculate("14-3/2"))
