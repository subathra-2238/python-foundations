# DSA-31: Linked List - Insert at a Given Position


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Existing linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(40)

node1.next = node2
node2.next = node3


# Insert 30 at position 2
new_node = Node(30)

position = 2

current = node1

for _ in range(position - 1):
    current = current.next


# Connect new node
new_node.next = current.next
current.next = new_node


# Traverse
current = node1

while current is not None:
    print(current.data)
    current = current.next