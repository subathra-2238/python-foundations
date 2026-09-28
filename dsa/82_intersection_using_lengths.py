class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Common part
node30 = Node(30)
node40 = Node(40)
node50 = Node(50)

node30.next = node40
node40.next = node50


# List A
head_a = Node(10)
head_a.next = Node(20)
head_a.next.next = node30


# List B
head_b = Node(5)
head_b.next = Node(15)
head_b.next.next = node30


def get_length(head):
    length = 0
    current = head

    while current is not None:
        length += 1
        current = current.next

    return length


def find_intersection(head_a, head_b):
    length_a = get_length(head_a)
    length_b = get_length(head_b)

    pointer_a = head_a
    pointer_b = head_b

    # Align both pointers
    if length_a > length_b:
        for _ in range(length_a - length_b):
            pointer_a = pointer_a.next

    elif length_b > length_a:
        for _ in range(length_b - length_a):
            pointer_b = pointer_b.next

    # Compare nodes
    while pointer_a is not pointer_b:
        pointer_a = pointer_a.next
        pointer_b = pointer_b.next

    return pointer_a


def display(head):
    current = head

    while current is not None:
        print(current.data, end=" → ")
        current = current.next

    print("None")


print("List A:")
display(head_a)

print("List B:")
display(head_b)

intersection = find_intersection(head_a, head_b)

if intersection is not None:
    print("Intersection point:", intersection.data)
else:
    print("No intersection.")