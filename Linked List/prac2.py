#create Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#assigning values
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)
Node6 = Node(6)

#linking Nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
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

#print the linked list
printNode(head)
