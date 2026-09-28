# DSA-20: Queue Operations

queue = []


# Enqueue
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)


# Peek - See the first element
print("Front element:", queue[0])


# Dequeue - Remove the first element
removed = queue.pop(0)

print("Removed:", removed)
print("Queue after dequeue:", queue)


# Check if empty
if len(queue) == 0:
    print("Queue is empty")
else:
    print("Queue is not empty")