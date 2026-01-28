#search for a element in linked list
#create a Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
#Assigning values
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)

#linking Nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

#funtion to search for a key in linked list
def search_elemn(head, key):
    curr = head
    while curr is not None:
        if curr.data == key:
            return True
        curr = curr.next
    return False

#head of the linked list
head = Node1
key = 30
if search_elemn(head, key):
    print(f"{key} is present in linked list")           


