#Insert a node at the beginning of a singly linked list.
#create a Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create nodes and assign values
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)

#linking nodes
Node1.next = Node2
Node2.next = Node3

#head of the linked list
head = Node1

#print function
def printNode(head):
    curr = head
    if head is None:
        print("Linked List is empty")
    while curr is not None:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")

#add a node at the beginning
new_node = Node(5)      
new_node.next = head
head = new_node     

#call print function
printNode(head)