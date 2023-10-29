# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head, val: int):

        # Solution 1
    # # Base case: If the head is None, return None
    #     if not head:
    #         return None

    #     # Recursively remove the value from the rest of the list
    #     head.next = self.removeElements(head.next, val)

    #     # Check if the current node's value is equal to val and return the next node
    #     return head if head.val != val else head.next

    # Solution 2
        # Create a dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next