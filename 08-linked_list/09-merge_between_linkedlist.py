

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def merge_two_linkedlist(list1, a, b, list2):
    
    count = 0
    current = list1
    dummyA = Node(0)
    tailA = dummyA

    while current and count < a:
        tailA.next = current
        tailA = tailA.next
        current = current.next
        count += 1

    while current and count <= b:
        current = current.next
        count += 1

    tailA.next = list2

    while tailA.next:
        tailA = tailA.next
    
    tailA.next = current

    return dummyA.next


def create_linkedlist(values):
    
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head


list1 = create_linkedlist([10,1,13,6,9,5])
list2 = create_linkedlist([1000000,1000001,1000002])

a = 3
b = 4

merged_list = merge_two_linkedlist(list1, a, b, list2)

current = merged_list
while current:
    print(current.value, end="->")
    current = current.next