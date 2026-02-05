#Hare and Tortoise Algorithm 
#class Node:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def hareAndTortoise(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 

        if slow == fast:
            return True
    return False