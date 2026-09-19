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
head.next.next.next.next.next.next = Node(2)


def find_frequency(head):
    frequency = {}
    current = head

    while current is not None:
        if current.data in frequency:
            frequency[current.data] += 1
        else:
            frequency[current.data] = 1

        current = current.next

    return frequency


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

frequency = find_frequency(head)

print("Frequency:")

for value, count in frequency.items():
    print(f"{value} → {count} time(s)")