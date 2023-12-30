class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        # Solution 3

        total_chars = Counter()
        
        for word in words:
            total_chars += Counter(word)

        word_count = len(words)
        return all(count % word_count == 0 for count in total_chars.values())

        # Solution 2

        # l = len(words)
        # s = sum(len(x) for x in words)
      
        # return s % l == 0 
        
        # Solution 1

        # ans = []

        # for x in words:
        #     ans.append(len(x))

        # ans.sort()

        # return ans[-1] - ans[0] <= 2 and len(ans) % 2 != 0 
    
        # Fastest online
    
        # joint = ''.join(words)
        # set1 = set(joint)
        
        # for i in set1 :
        #     if joint.count(i) % len(words) != 0 : return False 
        # return True