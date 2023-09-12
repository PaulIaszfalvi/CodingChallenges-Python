class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        # Solution 1
        
        # strArr = [s[i:i + k] for i in range(0, len(s), k)]
   
        # maxCount = 0
        # vowels = "aeiou"

        # for e in strArr:

        #     currCount = 0

        #     for i in e:
        #         if i in vowels:
        #             currCount += 1

        #         maxCount = max(maxCount, currCount)

        # return maxCount

        # Solution 2

        maxCount = 0       
        currCount = 0           
        vowels = "aeiou"            
        
        for i, e in enumerate(s):
            #start moving out of former range
            if i >= k:
                if s[i-k] in vowels:
                    currCount -= 1
            #if current item is a vowel 
            if s[i] in vowels:
                currCount += 1
            maxCount = max(currCount, maxCount)
           
        return maxCount

s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))

s = "aeiou"
k = 2
print(Solution().maxVowels(s, k))

s = "leetcode"
k = 3
print(Solution().maxVowels(s, k))

s = "weallloveyou"
k = 7
print(Solution().maxVowels(s, k))


'''
Best Solution 

Intuition
We want the maximum count of any k-length substring of s. A sliding window seems appropriate.

Approach
Replace each of the characters in s with an int value: 1 for vowels, 0 otherwise (s will now be a list of ints). After that, the sum of all the elements of a k-length slice will be the count of vowels in that slice.

We'll return the maximum sum of any k-length slice (window) on s.

Complexity
Time complexity:
O(nnn) for an n-character string as we traverse s once to make the list of 1 and 0 values, and again to find the maximum sum of k consecutive elements.

Space complexity:
O(nnn). The list of 1's and 0's has length n for n input characters. Even though we replace the original s with the list of ints, that list is newly created (by a list comprehension) and doesn't allow the input string to be garbage collected as it still exists in the caller's scope.

Code
# Constant Dictionary of characters: vowels are 1, others are 0 (default)
VOWELS = defaultdict(int)
VOWELS['a'] = VOWELS['e'] = VOWELS['i'] = VOWELS['o'] = VOWELS['u'] = 1

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
      
        Replace characters in s with an int value: 1 for vowels, 0 otherwise.
        We'll return the maximum sum of any k-length window on s. 
        
        s = [VOWELS[c] for c in s]
        max_count = count = sum(s[:k])      # Both counts hold the initial sum
        for i in range(len(s) - k):         # Advance the window
            count += s[i + k] - s[i]        # Adjust the count
            if count > max_count:           # Keep the higher count
                max_count = count
        return max_count

'''