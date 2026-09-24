class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def first_equal_to_previous(head):
    if head is None or head.next is None:
        return None

    current = head

    while current.next is not None:
        if current.next.data == current.data:
            return current.next.data

        current = current.next

    return None


# Create linked list
head = Node(10)
head.next = Node(5)
head.next.next = Node(5)
head.next.next.next = Node(8)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(12)

result = first_equal_to_previous(head)

if result is not None:
    print("First equal value:", result)
else:
    print("No equal value found")