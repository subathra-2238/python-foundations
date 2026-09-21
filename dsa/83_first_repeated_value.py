class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(20)
head.next.next.next.next = Node(40)


def find_first_repeated(head):
    seen = set()
    current = head

    while current is not None:

        if current.data in seen:
            return current.data

        seen.add(current.data)
        current = current.next

    return None


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

result = find_first_repeated(head)

if result is not None:
    print("First repeated value:", result)
else:
    print("No repeated value.")