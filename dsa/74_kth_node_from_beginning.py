class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def find_kth_node(head, k):
    current = head
    position = 1

    while current is not None:
        if position == k:
            return current

        current = current.next
        position += 1

    return None


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Linked list:")
display(head)

k = 3
result = find_kth_node(head, k)

if result is not None:
    print(f"{k}rd node from the beginning:", result.data)
else:
    print("Position does not exist.")