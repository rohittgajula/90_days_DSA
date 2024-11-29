
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


def merge_two_lists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:
        if list1.value <= list2.value:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next


def create_linkedList(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

list1 = create_linkedList([1,3,5])
list2 = create_linkedList([2,4,6])

merged_list = merge_two_lists(list1, list2)

current = merged_list
while current:
    print(current.value, end="->")
    current = current.next

