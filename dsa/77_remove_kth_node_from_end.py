class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


head = Node(10)

head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)


def remove_kth_from_end(head, k):
    dummy = Node(0)
    dummy.next = head

    slow = dummy
    fast = dummy

    # Move fast k steps ahead
    for _ in range(k):
        if fast.next is None:
            return head

        fast = fast.next

    # Move both pointers
    while fast.next is not None:
        slow = slow.next
        fast = fast.next

    # Remove the kth node from the end
    slow.next = slow.next.next

    return dummy.next


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("Original linked list:")
display(head)

k = 2
head = remove_kth_from_end(head, k)

print("After removing kth node from the end:")
display(head)