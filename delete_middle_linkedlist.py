# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head.next:
            return None
        
        fast = head
        slow = head
        count = 0
        
        while fast and fast.next:
            print(fast.val, slow.val)
            prev = slow
            fast = fast.next.next
            slow = slow.next
            count += 1
            
        if count > 0:
            prev.next = slow.next
        # else:
        #     head = None       

        return head