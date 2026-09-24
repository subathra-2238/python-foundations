class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def last_greater_than_previous(head):
    if head is None or head.next is None:
        return None

    current = head
    result = None

    while current.next is not None:
        if current.next.data > current.data:
            result = current.next.data

        current = current.next

    return result


# Create linked list
head = Node(10)
head.next = Node(5)
head.next.next = Node(15)
head.next.next.next = Node(8)
head.next.next.next.next = Node(20)
head.next.next.next.next.next = Node(12)

result = last_greater_than_previous(head)

if result is not None:
    print("Last greater value:", result)
else:
    print("No greater value found")