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
    fast = head
    slow = head

    # Move fast pointer k positions ahead
    for _ in range(k):
        if fast is None:
            return None

        fast = fast.next

    # Move both pointers
    while fast is not None:
        slow = slow.next
        fast = fast.next

    return slow


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