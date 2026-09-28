# DSA-25: Circular Queue Basics

queue = [None, None, None]
max_size = 3

front = 0
rear = 0


# Add first element
queue[rear] = 10
rear = (rear + 1) % max_size

# Add second element
queue[rear] = 20
rear = (rear + 1) % max_size

# Add third element
queue[rear] = 30
rear = (rear + 1) % max_size

print("Queue:", queue)

# Remove first element
removed = queue[front]
queue[front] = None

front = (front + 1) % max_size

print("Removed:", removed)
print("Queue:", queue)

# Add new element
queue[rear] = 40
rear = (rear + 1) % max_size

print("Queue after circular insertion:", queue)