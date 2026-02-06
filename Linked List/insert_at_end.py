# Insert a node at a end of a singly linked list.
#create a Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create nodes and assign values
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)

#linking nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

#head of the linked list
head = Node1

#create a new node and insert at the end
new_node = Node(50)
curr = head
while curr.next is not None:
    curr = curr.next
curr.next = new_node

#print function
def printNode(head):
    curr = head
    if head is None:
        print("Linked List is empty")
    while curr is not None:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")

#call print function
printNode(head)