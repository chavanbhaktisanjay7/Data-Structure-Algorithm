#count the number of nodes in singly linked list

#create class node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#create nodes and assign values 

Node1 = Node(5)
Node2 = Node(10)
Node3 = Node(15)
Node4 = Node(20)
Node5 = Node(25)
Node6 = Node(30)

#linking of nodes

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6

#assign head of the linked list

head = Node1

#print function
def printNode(head):
    curr = head
    count = 0
    if head is None:
        print("Linked List if empty")
    while curr is not None:
        print(curr.data,end="->")        
        count = count+1
        curr = curr.next
    print("None")
    print("Number of Nodes in linked list are -",count)


#call print function
printNode(head)

