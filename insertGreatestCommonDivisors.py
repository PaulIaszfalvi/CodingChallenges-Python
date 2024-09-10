# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

      # Solution 3

      # Edge case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        current = head
        
        while current and current.next:
            # Compute GCD of the current node's value and the next node's value
            gcd_value = math.gcd(current.val, current.next.val)
            
            # Insert a new node with the GCD value between current and current.next
            new_node = ListNode(gcd_value, current.next)
            current.next = new_node
            
            # Move to the next pair of nodes
            current = new_node.next
        
        return head

      # Solution 2

      # Edge case: if the list is empty or has only one node
        if not head or not head.next:
            return head
        
        # Initialize pointers
        first, second = head, head.next
        
        while second:
            # Compute GCD of the current node's value and the next node's value
            value = 1
            for x in range(1, min(first.val, second.val) + 1):
                if first.val % x == 0 and second.val % x == 0:
                    value = x
            
            # Insert a new node with the GCD value between first and second
            temp = ListNode(value, second)
            first.next = temp
            
            # Move to the next pair of nodes
            first = second
            second = second.next
        
        return head
    

      # Solution 1
        
        first, second = head, head.next

        while second:
            
            value = 1

            for x in range(1, max(first.val, second.val)):

                if x > first.val or x > second.val:
                    break

                if first.val % x == 0 and second.val % x == 0:
                    value = x

            temp = ListNode(value, first.next)
            first.next = temp
            first = second
            second = second.next
        
        return head
            
                

                

            
