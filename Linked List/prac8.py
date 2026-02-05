#check if the list is palindrome or not
#class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#creating nodes and assigning values
Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(1) 

#linking nodes
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4

#head of the linked list
head = Node1

def isPalindrome(head):
    #0 or 1 is palindrome
    if head and head.next is None:
        return True
    
    #find the middle of the linked list
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    #reverse the second half of the linkd list
    prev = None
    curr = slow
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    #compare the first half and the reversed second half
    first = head
    second = prev
    while second:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
    return True

print(isPalindrome(head))











































#hare and tortoise approach to check if linked list is palindrome
# def isPalindrome(head):
#     slow = head
#     fast = head
#     stack = []
    
#     while fast is not None and fast.next is not None:
#         stack.append(slow.data)
#         slow = slow.next
#         fast = fast.next.next
    
#     if fast is not None:
#         slow = slow.next
    
#     while slow is not None:
#         top = stack.pop()
        
#         if top != slow.data:
#             return False
#         slow = slow.next
    
#     return True


