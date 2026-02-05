#check if the list is palindrome or not
#class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating nodes and assigning values
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(2)
Node4 = Node(1) 

#linking nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

#head of the linked list
head = Node1

#hare and tortoise approach to check if linked list is palindrome
def isPalindrome(head):
    slow = head
    fast = head
    stack = []
    
    while fast is not None and fast.next is not None:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    
    if fast is not None:
        slow = slow.next
    
    while slow is not None:
        top = stack.pop()
        
        if top != slow.data:
            return False
        slow = slow.next
    
    return True

#### yet to complete the code for checking palindrome in linked list
