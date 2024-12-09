class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def reorder_list(head):
    # finding the middle
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second-half
    second = slow.next
    prev = None
    slow.next = None            # we are spiting linkedlist
    while second:
        temp = second.next
        second.next = prev
        prev = second
        second = temp

    # merge two half
    first = head
    second = prev
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2
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


linked_list = create_linkedlist([1,2,3,4])

current = reorder_list(linked_list)
while current:
    print(current.value, end='->')
    current = current.next


    