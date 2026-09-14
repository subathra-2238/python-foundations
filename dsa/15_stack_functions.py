# DSA-15: Stack using Functions

stack = []


def push(stack, value):
    stack.append(value)


def pop(stack):
    if len(stack) == 0:
        return None

    return stack.pop()


def peek(stack):
    if len(stack) == 0:
        return None

    return stack[-1]


# Push elements
push(stack, 10)
push(stack, 20)
push(stack, 30)

print("Stack:", stack)

# Peek
print("Top element:", peek(stack))

# Pop
print("Removed:", pop(stack))

print("Stack after pop:", stack)