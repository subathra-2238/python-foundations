class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(25)
head.next.next = Node(7)
head.next.next.next = Node(40)
head.next.next.next.next = Node(15)


def find_second_largest(head):
    if head is None or head.next is None:
        return None

    largest = float("-inf")
    second_largest = float("-inf")

    current = head

    while current is not None:

        if current.data > largest:
            second_largest = largest
            largest = current.data

        elif current.data > second_largest and current.data != largest:
            second_largest = current.data

        current = current.next

    if second_largest == float("-inf"):
        return None

    return second_largest


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

second_largest = find_second_largest(head)

print("Second largest value:", second_largest)