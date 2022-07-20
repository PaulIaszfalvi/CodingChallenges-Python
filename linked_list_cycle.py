# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution(object):
#     def hasCycle(self, head):
        
#         map = {}
        
#         if head != None:
        
#             while head.next != None:

#                 map[head] = map.get(head, 0) +1

#                 if map[head] > 1:
#                     return True

#                 head = head.next

#         return False

class Solution(object):
    def hasCycle(self, head):
        
        tortoise = hare = head    
        
        while hare and hare.next :
                
            tortoise = tortoise.next
            hare = hare.next.next
                
            if tortoise == hare:
                return True
        
        return False
        