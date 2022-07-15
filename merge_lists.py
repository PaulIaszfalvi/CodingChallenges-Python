from typing import Optional

from idna import valid_contextj

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MergeLists: 
 
    def merge(self, L1: Optional[ListNode], L2: Optional[ListNode]) -> Optional[ListNode]:
        L3 = result = ListNode(0)

      
        while L1 and L2:         
            
            if L1.val <= L2.val:
                #print(L1.val)
                L3.next = L1
                L1 = L1.next          
            else:
                #print(L2.val)
                L3.next = L2
                L2 = L2.next
            L3 = L3.next

        if L1:
            L3.next = L1
        if L2:
            L3.next = L2

        return result.next

l1n3 = ListNode(4, None)
l1n2 = ListNode(3, l1n3)
l1n1 = ListNode(1, l1n2)
L1 = l1n1

l2n3 = ListNode(4, None)
l2n2 = ListNode(2, l2n3)
l2n1 = ListNode(1, l2n2)
L2 = l2n1
 
m = MergeLists()
print(m.merge(L1, L2))

class MergeArrayList: 

    def mergeLists(self, L1, L2):

        newList = []
        l1_itr = 0;
        l2_itr = 0

        while l1_itr < len(L1) and l2_itr < len(L2):

            if L1[l1_itr] <= L2[l2_itr]:
                newList.append(L1[l1_itr])
                l1_itr += 1
            elif L1[l1_itr] > L2[l2_itr]:
                newList.append(L2[l2_itr])
                l2_itr += 1

        if l1_itr < len(L1):
            newList = newList + L1[l1_itr::]
        else:
            newList = newList + L2[l2_itr::]    
        return newList

L1 = [1, 2, 4, 6, 7, 9]
L2 = [1, 3, 5, 10]

merge = MergeArrayList();
print(merge.mergeLists(L1, L2))