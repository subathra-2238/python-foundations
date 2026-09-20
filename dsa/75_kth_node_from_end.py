class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def find_kth_from_end(head, k):
    current = head
    length = 0

    # Find length
    while current is not None:
        length += 1
        current = current.next

    # Check if k is valid
    if k <= 0 or k > length:
        return None

    # Move to kth node from beginning
    current = head

    for _ in range(length - k):
        current = current.next

    return current


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

k = 2
result = find_kth_from_end(head, k)

if result is not None:
    print(f"{k}nd node from the end:", result.data)
else:
    print("Position does not exist.")