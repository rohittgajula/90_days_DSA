

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def isPalindrome(head):
    if not head:
        return False
    
    # find mid value
    fast = head
    slow = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse the 2nd half
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # check for palindrome
    left = head
    right = prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    return True

def create_linkedlist(values):
    if not values:
        return None

    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

linked_list = create_linkedlist([1,2,2,1])
print(isPalindrome(linked_list))

# current = linked_list
# while current:
#     print(current.value, end="->")
#     current = current.next