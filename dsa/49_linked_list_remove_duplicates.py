# DSA-49: Linked List - Remove Duplicates


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


# Create linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(10)
node4 = Node(30)
node5 = Node(20)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


# Remove duplicates
current = node1

while current is not None:

    runner = current

    while runner.next is not None:

        if runner.next.data == current.data:
            runner.next = runner.next.next
        else:
            runner = runner.next

    current = current.next


# Display linked list
current = node1

while current is not None:
    print(current.data)
    current = current.next