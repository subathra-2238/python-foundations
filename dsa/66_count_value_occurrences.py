class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(1)

head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(2)


def count_occurrences(head, value):
    count = 0
    current = head

    while current is not None:
        if current.data == value:
            count += 1

        current = current.next

    return count


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

value = 2
count = count_occurrences(head, value)

print(f"{value} appears {count} times.")