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

#Linking Nodes
Node1.next = Node2
Node2.next = Node3  
Node3.next = Node4

# #create a new and insert at the beginning
head = Node1
start_new_node = Node(50)
start_new_node.next = head
head = start_new_node

#create a new and insert at the end
end_new_node = Node(60)
curr = head
while curr.next is not None:
    curr = curr.next
curr.next = end_new_node

#create a new and insert at a given position
position_new_node = Node(70)
count = 0
curr = head
position = 2
while count < position-1 and curr is not None:
    curr = curr.next
    count += 1
position_new_node.next = curr.next
curr.next = position_new_node   

#print the curr traversed linkd list
curr = head
while curr is not None:
    print(curr.data, end = " -> " )
    curr = curr.next
print("None") 

