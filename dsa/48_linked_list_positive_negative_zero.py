# DSA-48: Linked List - Count Positive, Negative and Zero


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(-5)
node3 = Node(0)
node4 = Node(25)
node5 = Node(-15)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Count elements
current = node1

positive_count = 0
negative_count = 0
zero_count = 0

while current is not None:

    if current.data > 0:
        positive_count += 1

    elif current.data < 0:
        negative_count += 1

    else:
        zero_count += 1

    current = current.next


print("Positive elements:", positive_count)
print("Negative elements:", negative_count)
print("Zero elements:", zero_count)