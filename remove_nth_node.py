# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # Solution Iterative

        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move second pointer n+1 steps ahead
        for _ in range(n + 1):
            second = second.next

        # Move both pointers until the second pointer reaches the end
        while second:
            first = first.next
            second = second.next

        # Remove the N-th node
        first.next = first.next.next

        return dummy.next

        # Solution Recursive

        def rem(node, n):
            if not node:
                return None, 0

            next_node, count = rem(node.next, n)

            if count == n-1:
                return next_node, count + 1

            node.next = next_node
            return node, count + 1

        result, _ = rem(head, n)
        return result