# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # Solution 1

        # myList = []

        # pointer = head

        # while pointer and pointer.next:
        #     myList.append(pointer)
        #     pointer.next

        # forward = 0
        # backward = len(myList)-1
        # max_val = 0

        # while forward < backward:
        #     max_val = max(myList[forward].val + myList[backward].val, max_val)
        #     forward += 1
        #     backward -= 1

        # return max_val
    
head = [5,4,2,1]
print(Solution().pairSum(head))

head = [4,2,2,3]
print(Solution().pairSum(head))