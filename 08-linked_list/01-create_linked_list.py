

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, key):
        current = self.head

        # If the head node is to be deleted
        if current and current.data == key:
            self.head = current.next
            current = None
            return

        # Find the node to be deleted
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the key was not found
        if not current:
            print("Value not found in the list.")
            return

        # Unlink the node
        prev.next = current.next
        current = None

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    
    # Insert operations
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    
    print("Linked List after insertions:")
    ll.traverse()

    # Search operation
    print("Search for 30:", ll.search(30))
    print("Search for 50:", ll.search(50))

    # Delete operation
    ll.delete_node(20)
    print("Linked List after deletion of 20:")
    ll.traverse()
    
    ll.delete_node(50)  # Trying to delete a non-existing node
