class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def last_local_peak(head):
    if head is None or head.next is None or head.next.next is None:
        return None

    previous = head
    current = head.next
    result = None

    while current.next is not None:
        if current.data > previous.data and current.data > current.next.data:
            result = current.data

        previous = current
        current = current.next

    return result


# Create linked list
head = Node(5)
head.next = Node(10)
head.next.next = Node(6)
head.next.next.next = Node(12)
head.next.next.next.next = Node(8)
head.next.next.next.next.next = Node(15)
head.next.next.next.next.next.next = Node(7)

result = last_local_peak(head)

if result is not None:
    print("Last local peak:", result)
else:
    print("No local peak found")