class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(-5)
head.next.next = Node(20)
head.next.next.next = Node(-15)
head.next.next.next.next = Node(0)


def find_sum(head):
    total = 0

    current = head

    while current is not None:
        total += current.data
        current = current.next

    return total


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

total = find_sum(head)

print("Sum of all values:", total)