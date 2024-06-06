class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        # Solution 2      
         if len(hand) % groupSize != 0:
            return False
            
        card_counts = Counter(hand)
        
        for card in sorted(card_counts):
            count = card_counts[card]
            if count > 0:
                # Check if there are enough cards to form a group
                for i in range(1, groupSize):
                    if card + i not in card_counts or card_counts[card + i] < count:
                        return False
                    card_counts[card + i] -= count
                card_counts[card] -= count * groupSize
        
        return True

        # Solution 1

        def isContinuous(lst):
            if not lst:
                return False  
            
            for i in range(1, len(lst)):
                if lst[i] != lst[i-1] + 1:
                    return False  
            return True

        def getIndex(list_2d, groupSize):
            for i, sublist in enumerate(list_2d):
                if len(sublist) < groupSize:
                    return i
            return -1

        if len(hand) % groupSize != 0:
            return False

        hand.sort()
        d = {x: hand.count(x) for x in hand}        
        ans = [[] for _ in range(groupSize)]

        for key, value in d.items():

            idx = getIndex(ans, groupSize)

            while value > 0:          
                ans[idx].append(key)  # Append the key to the sublist
                value -= 1  # Decrement the value
                idx += 1      
                
        # Check if all sublists are continuous
        return all(isContinuous(sublist) for sublist in ans)
