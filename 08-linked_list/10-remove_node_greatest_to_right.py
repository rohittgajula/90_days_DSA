class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def remove_node(head):
    # Reverse the linked list
    reversed_head = reverse_list(head)
    
    # Traverse the reversed list
    max_value = float('-inf')
    dummy = Node(0)
    tail = dummy
    current = reversed_head
    
    while current:
        if current.value >= max_value:
            max_value = current.value
            tail.next = current
            tail = tail.next
        current = current.next
    
    # Ensure the new list ends
    tail.next = None
    
    # Reverse the list back to the original order
    return reverse_list(dummy.next)

def create_linkedlist(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Test the function
linked_list = create_linkedlist([5, 2, 13, 3, 8])
removed_list = remove_node(linked_list)

# Print the result
current = removed_list
while current:
    print(current.value, end="->")
    current = current.next
print("None")
