

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


def middle(head):
    if not head:
        return None
    
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


def create_linkedlist(values):
    if not values:
        return None
    
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

linked_list = create_linkedlist([1,2,3,4,5])

middle_linkedlist = middle(linked_list)

current = middle_linkedlist
while current:
    print(current.value, end="->")
    current = current.next


    