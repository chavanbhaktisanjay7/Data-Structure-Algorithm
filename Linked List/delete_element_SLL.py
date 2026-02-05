#class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#assigning values
Node1 = Node(5)
Node2 = Node(10)
Node3 = Node(15)    
Node4 = Node(20)
Node5 = Node(25)
Node6 = Node(30)

# linking Nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5  
Node5.next = Node6    

#assigning Node1 as head
head = Node1

#print Node
def printNode(head):
    curr = head
    # if head is None:
    #     print("Linked List is empty")
    while curr is not None:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")

#function to delete a head node
def delete_head(head):
    curr = head
    head = curr.next
    printNode(head)

#Call Function
#delete_head(head)

#function to delete a tail node
def delete_tail(head):
    curr = head 
    if head is None:
       print("Linked List is empty")
    
    while curr.next.next is not  None:
       curr = curr.next
       
    curr.next = None
    printNode(head)

#call Function
# delete_tail(head)

#function to delete a node at given position
def delete_position(head, position):
    curr = head
    if head is None:
        print("Linked List is empty")

    while position-1 >0 and curr is not None:
        prev = curr
        curr = curr.next
        position -=1
    prev.next = curr.next
    printNode(head)


#call Function
delete_position(head, 2)