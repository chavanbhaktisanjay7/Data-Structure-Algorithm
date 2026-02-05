#Add elements in a doubly linked list and print all elements.
#Create a Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

#Create a Doubly Linked List class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    #Insert a node at the beginning
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head :
            self.head.prev = new_node
            new_node.prev = None
        self.head = new_node

    #Insert a node at the end
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return 
        curr = self.head
        while curr.next is not None :
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    #Print the doubly linked list
    def print_list(self):
        curr = self.head
        while curr is not None:
            print(curr.data, end = " <-> ")
            curr = curr.next
        print("None")

#Create a doubly linked list and add elements
dll = DoublyLinkedList()
dll.insert_at_head(00)
dll.insert_at_end(99)
dll.print_list()