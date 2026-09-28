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


def remove_all_duplicates(head):
    frequency = {}
    current = head

    # Count frequencies
    while current is not None:
        frequency[current.data] = frequency.get(current.data, 0) + 1
        current = current.next

    # Remove values that occur more than once
    dummy = Node(0)
    dummy.next = head

    previous = dummy
    current = head

    while current is not None:

        if frequency[current.data] > 1:
            previous.next = current.next
        else:
            previous = current

        current = current.next

    return dummy.next


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Original linked list:")
display(head)

head = remove_all_duplicates(head)

print("After removing all duplicate values:")
display(head)