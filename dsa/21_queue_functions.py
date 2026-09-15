# DSA-21: Queue using Functions

queue = []


def enqueue(queue, value):
    queue.append(value)


def dequeue(queue):
    if len(queue) == 0:
        return None

    return queue.pop(0)


def peek(queue):
    if len(queue) == 0:
        return None

    return queue[0]


# Enqueue elements
enqueue(queue, 10)
enqueue(queue, 20)
enqueue(queue, 30)

print("Queue:", queue)

# Peek
print("Front element:", peek(queue))

# Dequeue
print("Removed:", dequeue(queue))

print("Queue after dequeue:", queue)