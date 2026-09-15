# DSA-29: Linked List Insert at Beginning


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
new_node = Node(5)

# Connect new node to the old first node
new_node.next = node1

# Make new node the first node
node1 = new_node


# Traverse the linked list
current = node1

while current is not None:
    print(current.data)
    current = current.next