# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_list = head

        while new_list and new_list.next:
            if new_list.val == new_list.next.val:             
                new_list.next = new_list.next.next
            else:
                new_list = new_list.next

        return head