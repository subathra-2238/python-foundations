class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(40)
head.next.next.next = Node(50)


def insert_sorted(head, value):
    new_node = Node(value)

    # Insert at beginning
    if head is None or value <= head.data:
        new_node.next = head
        return new_node

    current = head

    # Find the correct position
    while current.next is not None and current.next.data < value:
        current = current.next

    new_node.next = current.next
    current.next = new_node

    return head


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Original linked list:")
display(head)

value = 30
head = insert_sorted(head, value)

print("After inserting", value, ":")
display(head)