

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def remove_duplicates(head):
    if head is None:
        return None
    
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return head

def create_linkedlist(values):
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

linked_list = create_linkedlist([1,1,2])

removed_list = remove_duplicates(linked_list)

current = removed_list
while current:
    print(current.value, end="->")
    current = current.next


