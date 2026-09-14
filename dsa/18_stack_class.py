# DSA-18: Stack using a Class


class Stack:

    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    # Push
    def push(self, value):
        if len(self.stack) < self.max_size:
            self.stack.append(value)
            print("Pushed:", value)
        else:
            print("Stack Overflow")

    # Pop
    def pop(self):
        if len(self.stack) > 0:
            print("Popped:", self.stack.pop())
        else:
            print("Stack Underflow")

    # Peek
    def peek(self):
        if len(self.stack) > 0:
            print("Top element:", self.stack[-1])
        else:
            print("Stack is empty")

    # Display
    def display(self):
        print("Stack:", self.stack)


# Create Stack object
s = Stack(3)

s.push(10)
s.push(20)
s.push(30)

s.display()

s.peek()

s.push(40)

s.pop()

s.display()