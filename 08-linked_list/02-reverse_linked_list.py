
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def reverse_linkedlist(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def create_linkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

linked_list = create_linkedList([1,2,3,4])

reversed_list = reverse_linkedlist(linked_list)

current = reversed_list
while current:
    print(current.value, end="->")
    current = current.next

