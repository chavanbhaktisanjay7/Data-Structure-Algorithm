#Reverse the singly linked list
#creat class Node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating nodes and assigning values
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

#yet to complete the code 