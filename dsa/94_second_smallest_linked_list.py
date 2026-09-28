class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(25)
head.next.next = Node(7)
head.next.next.next = Node(40)
head.next.next.next.next = Node(15)


def find_second_smallest(head):
    if head is None or head.next is None:
        return None

    smallest = float("inf")
    second_smallest = float("inf")

    current = head

    while current is not None:

        if current.data < smallest:
            second_smallest = smallest
            smallest = current.data

        elif current.data < second_smallest and current.data != smallest:
            second_smallest = current.data

        current = current.next

    if second_smallest == float("inf"):
        return None

    return second_smallest


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

second_smallest = find_second_smallest(head)

print("Second smallest value:", second_smallest)