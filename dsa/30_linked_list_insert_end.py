# DSA-30: Linked List Insert at End


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Existing linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3


# Create new node
new_node = Node(40)


# Find the last node
current = node1

while current.next is not None:
    current = current.next


# Connect last node to new node
current.next = new_node


# Traverse the linked list
current = node1

while current is not None:
    print(current.data)
    current = current.next
    