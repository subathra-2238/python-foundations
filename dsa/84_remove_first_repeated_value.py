class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(40)


def remove_first_repeated(head):
    seen = set()
    current = head
    previous = None

    while current is not None:

        if current.data in seen:
            previous.next = current.next
            return head

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

head = remove_first_repeated(head)

print("After removing first repeated value:")
display(head)