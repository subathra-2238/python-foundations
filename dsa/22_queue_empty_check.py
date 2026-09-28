# DSA-22: Queue Empty Check and Underflow

queue = []


# Try to dequeue from an empty queue
if len(queue) == 0:
    print("Queue Underflow")
else:
    print("Removed:", queue.pop(0))


# Add elements
queue.append(10)
queue.append(20)

print("Queue:", queue)


# Dequeue
if len(queue) == 0:
    print("Queue Underflow")
else:
    print("Removed:", queue.pop(0))

print("Queue after dequeue:", queue)