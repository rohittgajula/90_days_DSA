

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


def remove_element(head, value):

    while head is not None and head.value == value:
        head = head.next

    if head is None:
        return None

    current = head
    while current.next is not None:
        if current.next.value == value:
            current.next = current.next.next
        else:
            current = current.next
    return head

def create_linkedlist(values):
    if values is None:
        return None
    
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


linked_list = create_linkedlist([1,2,6,3,4,5,6])

value = 6
removed_elements = remove_element(linked_list, value)

current = removed_elements
while current:
    print(current.value, end="->")
    current = current.next

    