# DSA-17: Stack Overflow and Underflow

stack = []
max_size = 3


# Push
if len(stack) < max_size:
    stack.append(10)
    print("Pushed:", 10)
else:
    print("Stack Overflow")


if len(stack) < max_size:
    stack.append(20)
    print("Pushed:", 20)
else:
    print("Stack Overflow")


if len(stack) < max_size:
    stack.append(30)
    print("Pushed:", 30)
else:
    print("Stack Overflow")


# Try to push when full
if len(stack) < max_size:
    stack.append(40)
    print("Pushed:", 40)
else:
    print("Stack Overflow")


print("Stack:", stack)


# Pop
if len(stack) > 0:
    print("Popped:", stack.pop())
else:
    print("Stack Underflow")