class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def first_local_valley(head):
    if head is None or head.next is None or head.next.next is None:
        return None

    previous = head
    current = head.next

    while current.next is not None:
        if current.data < previous.data and current.data < current.next.data:
            return current.data

        previous = current
        current = current.next

    return None


# Create linked list
head = Node(10)
head.next = Node(5)
head.next.next = Node(12)
head.next.next.next = Node(6)
head.next.next.next.next = Node(15)
head.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next = Node(20)

result = first_local_valley(head)

if result is not None:
    print("First local valley:", result)
else:
    print("No local valley found")