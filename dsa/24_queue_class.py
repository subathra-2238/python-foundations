# DSA-24: Queue using a Class


class Queue:

    def __init__(self, max_size):
        self.queue = []
        self.max_size = max_size

    # Enqueue
    def enqueue(self, value):
        if len(self.queue) < self.max_size:
            self.queue.append(value)
            print("Enqueued:", value)
        else:
            print("Queue Overflow")

    # Dequeue
    def dequeue(self):
        if len(self.queue) > 0:
            print("Dequeued:", self.queue.pop(0))
        else:
            print("Queue Underflow")

    # Peek
    def peek(self):
        if len(self.queue) > 0:
            print("Front element:", self.queue[0])
        else:
            print("Queue is empty")

    # Display
    def display(self):
        print("Queue:", self.queue)


# Create Queue object
q = Queue(3)

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()

q.peek()

q.enqueue(40)

q.dequeue()

q.display()