# DSA-16: Stack Empty Check

stack = []

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Removed:", stack.pop())


stack.append(10)
stack.append(20)

print("Stack:", stack)

if len(stack) == 0:
    print("Stack is empty")
else:
    print("Removed:", stack.pop())

print("Stack after pop:", stack)