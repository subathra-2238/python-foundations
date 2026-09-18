# DSA-52: Sorted Linked List - Insert an Element


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create sorted linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(40)
node4 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4


# Value to insert
value = 30
new_node = Node(value)


# Insert at beginning if needed
if new_node.data < node1.data:
    new_node.next = node1
    node1 = new_node

else:
    current = node1

    # Find correct position
    while current.next is not None and current.next.data < value:
        current = current.next

    # Insert new node
    new_node.next = current.next
    current.next = new_node


# Display linked list
current = node1

while current is not None:
    print(current.data)
    current = current.next