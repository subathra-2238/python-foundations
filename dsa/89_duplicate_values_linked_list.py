class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(40)
head.next.next.next.next.next = Node(30)
head.next.next.next.next.next.next = Node(50)


def find_duplicate_values(head):
    frequency = {}
    current = head

    # Count frequencies
    while current is not None:
        frequency[current.data] = frequency.get(current.data, 0) + 1
        current = current.next

    # Find duplicate values
    duplicates = []

    for value, count in frequency.items():
        if count > 1:
            duplicates.append(value)

    return duplicates


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

result = find_duplicate_values(head)

print("Duplicate values:", result)