

# using two pointers
def isPalindrome(nums):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True
nums = [1,2,2,1]
print(isPalindrome(nums))

# ----------------------------------------

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def is_palindrome(head):
    fast = head
    slow = head

    # find the middle
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # reverse the second half
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # check palindrome
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

print(is_palindrome(linked_list))

current = linked_list
while current:
    print(current.value, end="->")
    current = current.next


