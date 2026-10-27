
def evaluate_rpn(tokens):
    stack = []

    for token in tokens:
        if token in {"+", "-", "*", "/"}:
            b = stack.pop()
            a = stack.pop()

            if token == "+":
                result = a + b
            elif token == "-":
                result = a - b
            elif token == "*":
                result = a * b
            else:
                # Division truncated toward zero
                result = int(a / b)

            stack.append(result)
        else:
            stack.append(int(token))

    return stack[0]


print(evaluate_rpn(["2", "1", "+", "3", "*"]))
print(evaluate_rpn(["4", "13", "5", "/", "+"]))
print(evaluate_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
