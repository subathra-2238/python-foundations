class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Common nodes
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


def find_intersection(head_a, head_b):
    pointer_a = head_a
    pointer_b = head_b

    while pointer_a is not pointer_b:

        if pointer_a is None:
            pointer_a = head_b
        else:
            pointer_a = pointer_a.next

        if pointer_b is None:
            pointer_b = head_a
        else:
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