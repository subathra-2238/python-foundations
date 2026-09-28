# DSA-26: Circular Queue using a Class


class CircularQueue:

    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.front = 0
        self.rear = 0
        self.count = 0

    # Enqueue
    def enqueue(self, value):
        if self.count == self.max_size:
            print("Queue Overflow")
            return

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.max_size
        self.count += 1

        print("Enqueued:", value)

    # Dequeue
    def dequeue(self):
        if self.count == 0:
            print("Queue Underflow")
            return

        removed = self.queue[self.front]
        self.queue[self.front] = None

        self.front = (self.front + 1) % self.max_size
        self.count -= 1

        print("Dequeued:", removed)

    # Peek
    def peek(self):
        if self.count == 0:
            print("Queue is empty")
        else:
            print("Front element:", self.queue[self.front])

    # Display
    def display(self):
        print("Queue:", self.queue)


# Create circular queue
q = CircularQueue(3)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.dequeue()

q.enqueue(40)

q.display()

q.peek()