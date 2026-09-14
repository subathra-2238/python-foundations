# DSA-19: Queue Basics

queue = []

# Enqueue - Add elements
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue:", queue)

# Dequeue - Remove first element
removed = queue.pop(0)

print("Removed:", removed)
print("Queue after dequeue:", queue)