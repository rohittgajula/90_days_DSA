

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


linked_list = create_linkedlist([1,1,2,2,3,4,6,7,7])

removed_elements_list = remove_element(linked_list, value = 1)

current = removed_elements_list
while current:
    print(current.value, end="->")
    current = current.next

