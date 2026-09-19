class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(4)

head.next = Node(2)
head.next.next = Node(4)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(3)
head.next.next.next.next.next.next = Node(1)


def remove_duplicates(head):
    seen = set()
    current = head
    previous = None

    while current is not None:
        if current.data in seen:
            previous.next = current.next
        else:
            seen.add(current.data)
            previous = current

        current = current.next

    return head


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Original linked list:")
display(head)

head = remove_duplicates(head)

print("After removing duplicates:")
display(head)