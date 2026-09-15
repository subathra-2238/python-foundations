# DSA-23: Queue Overflow and Underflow

queue = []
max_size = 3


# Enqueue
if len(queue) < max_size:
    queue.append(10)
    print("Enqueued:", 10)
else:
    print("Queue Overflow")


if len(queue) < max_size:
    queue.append(20)
    print("Enqueued:", 20)
else:
    print("Queue Overflow")


if len(queue) < max_size:
    queue.append(30)
    print("Enqueued:", 30)
else:
    print("Queue Overflow")


# Try to enqueue when full
if len(queue) < max_size:
    queue.append(40)
    print("Enqueued:", 40)
else:
    print("Queue Overflow")


print("Queue:", queue)


# Dequeue
if len(queue) > 0:
    print("Dequeued:", queue.pop(0))
else:
    print("Queue Underflow")