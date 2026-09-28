# DSA-14: Stack Operations

stack = []


# Push
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack:", stack)


# Peek
print("Top element:", stack[-1])


# Pop
removed = stack.pop()

print("Removed:", removed)
print("Stack after pop:", stack)


# Check if empty
if len(stack) == 0:
    print("Stack is empty")
else:
    print("Stack is not empty")