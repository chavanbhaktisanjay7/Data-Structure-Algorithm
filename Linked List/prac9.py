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
Node5 = Node(50)

#linking nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

#head of the linked list
head = Node1

#print the linked list
def printList(head):
    curr = head
    while curr:
        print(curr.data, end = " -> ")
        curr = curr.next
    print("None")

def reverseList(head):
    prev = None
    curr = head
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    return prev

print("Original Linked List:")
printList(head) 
reversed_head = reverseList(head)
print("Reversed Linked List:")
printList(reversed_head)
