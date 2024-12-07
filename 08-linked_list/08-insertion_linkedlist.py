class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


def find_intersection(headA, headB):
    visited = set()
    currentA = headA
    currentB = headB

    # Traverse list A and store nodes in a set
    while currentA:
        visited.add(currentA)
        currentA = currentA.next

    # Traverse list B and check if any node is already in the set
    while currentB:
        if currentB in visited:
            return currentB  # Intersection found
        currentB = currentB.next

    return None  # No intersection


def create_linked_lists(intersectVal, listA, listB, skipA, skipB):
    # Create two separate linked lists
    headA = Node(listA[0])
    currentA = headA
    for value in listA[1:]:
        currentA.next = Node(value)
        currentA = currentA.next

    headB = Node(listB[0])
    currentB = headB
    for value in listB[1:]:
        currentB.next = Node(value)
        currentB = currentB.next

    # Create the intersection node
    intersection = None
    if intersectVal is not None:
        intersection = Node(intersectVal)

    # Attach the intersection to listA at skipA
    currentA = headA
    for _ in range(skipA):
        currentA = currentA.next
    currentA.next = intersection

    # Attach the intersection to listB at skipB
    currentB = headB
    for _ in range(skipB):
        currentB = currentB.next
    currentB.next = intersection

    # Extend the intersection if there are extra values in listA or listB
    current = intersection
    for value in listA[skipA + 1:]:
        current.next = Node(value)
        current = current.next

    return headA, headB


# Input
intersectVal = 8
listA = [4, 1, 8, 4, 5]
listB = [5, 6, 1, 8, 4, 5]
skipA = 2
skipB = 3

# Create linked lists with intersection
headA, headB = create_linked_lists(intersectVal, listA, listB, skipA, skipB)

# Find intersection
intersection = find_intersection(headA, headB)
print(f"Intersection Node: {intersection.value if intersection else None}")
