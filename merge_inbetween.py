# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:

        # Revised (Online)
        
        ptr = list1
        for _ in range(a - 1):
            ptr = ptr.next
        
        qtr = ptr.next
        for _ in range(b - a + 1):
            qtr = qtr.next
        
        ptr.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = qtr
        
        return list1
        
        # Solution 1

        c = 0
        i = list1        
        e = list2

        while c < a-1:
            c += 1
            i = i.next

        t = i
        
        while c <= b:
            c += 1
            t = t.next

        while e and e.next:
            e = e.next

        i.next = list2
        e.next = t

        return list1
        
