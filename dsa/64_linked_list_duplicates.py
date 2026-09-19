class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)

head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(1)


def find_duplicates(head):
    seen = set()
    duplicates = set()

    current = head

    while current is not None:
        if current.data in seen:
            duplicates.add(current.data)
        else:
            seen.add(current.data)

        current = current.next

    return duplicates


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

duplicates = find_duplicates(head)

print("Duplicate values:", duplicates)