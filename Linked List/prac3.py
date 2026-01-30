#Create a singly linked list with 5 nodes and print all elements.
# create a Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create nodes and assign values

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)

#linking nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

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

#call print function
printNode(head)
