
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insertInBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def updateNode(self, position, data):
        if position <= 0:
            print("Invalid position!")
            return
        
        current = self.head
        count = 1
        while current is not None and count < position:
            current = current.next
            count += 1
        
        if current is None:
            print("Position out of bound!")
            return
        
        current.data = data

    def insertInMiddle(self, position, data):
        new_node = Node(data)

        if position <= 0:
            print("Invalid Position!")
            return
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return
        
        current = self.head
        count = 1
        while current is not None and count < position - 1:
            current = current.next
            count += 1

        if current is None:
            print("Position out of bound!")
            return
        
        new_node.next = current.next
        current.next = new_node

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def printList(self):
        current = self.head
        if current is None:
            print("None")
            return
        
        while current is not None:
            print(current.data, end="->")
            current = current.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insertInBegin(10)
    ll.insertAtEnd(100)
    ll.updateNode(1, 20)
    ll.insertInMiddle(2,15)
    print(f'length of linked-list : {ll.length()}')
    ll.printList()

