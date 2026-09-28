class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def first_less_than_previous(head):
    if head is None or head.next is None:
        return None

    current = head

    while current.next is not None:
        if current.next.data < current.data:
            return current.next.data

        current = current.next

    return None


# Create linked list
head = Node(20)
head.next = Node(15)
head.next.next = Node(18)
head.next.next.next = Node(10)
head.next.next.next.next = Node(25)

result = first_less_than_previous(head)

if result is not None:
    print("First less value:", result)
else:
    print("No less value found")