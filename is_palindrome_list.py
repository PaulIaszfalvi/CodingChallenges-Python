# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#solution 1
class Solution_One:
    def isPalindrome(self, head) -> bool:
        self.left = ListNode(0, head)

        def recursivefunc(head):
            if not head:
                return True
            
            right = recursivefunc(head.next)
            self.left = self.left.next
            return right and self.left.val == head.val

        return recursivefunc(head)

class Solution_Two:
    def isPalindrome(self, head) -> bool:
        
        if not head:
            return True

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None

        while slow:
            curr = slow
            slow = slow.next
            curr.next = prev
            prev = curr

        while prev:
            if prev.val != head.val:
                return False
            
            prev = prev.next
            head = head.next

        return True   

class Solution_Three:
    def isPalindrome(self, head) -> bool:
        p1 = head
        p2 = head

        stack = []

        if p1.next == None:
            return True

        while p2 is not None:
            stack.append(p1.val)
            p1 = p1.next
            p2 = p2.next.next

        while p1 is not None:
            
            if stack.pop() != p1.val:
                return False
            p1 = p1.next
        
        return True




node4 = ListNode(1)
node3 = ListNode(2, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

head = node1

print(Solution_One().isPalindrome(head))
print(Solution_Two().isPalindrome(head))