


def merge_lists(list1, list2):
    i = 0
    j = 0
    res = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    
    if i < len(list1):
        res.extend(list1[i:])
    elif j < len(list2):
        res.extend(list2[j:])

    return res


list1 = [1,3,5]
list2 = [2,4,6]
print(merge_lists(list1, list2))

# ------------------------------------------------

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

