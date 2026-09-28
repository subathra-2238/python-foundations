class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)

head.next = Node(4)
head.next.next = Node(7)
head.next.next.next = Node(4)
head.next.next.next.next = Node(9)


def find_last_occurrence(head, value):
    current = head
    position = 0
    last_position = -1

    while current is not None:
        if current.data == value:
            last_position = position

        current = current.next
        position += 1

    return last_position


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

value = 4
position = find_last_occurrence(head, value)

if position != -1:
    print(f"{value} last appears at position {position}.")
else:
    print(f"{value} was not found.")