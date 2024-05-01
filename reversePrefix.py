class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        # Solution 3

        # Find the index of the target character 'ch'
        index = word.find(ch)
        
        def reverse(s):
            if s == '':
                return ''

            return s[-1] + reverse(s[:-1])

        return reverse(word[:index+1]) + word[index+1:]

        # Solution 2

        # Find the index of the target character 'ch'
        index = word.find(ch)
           
        prefix = word[:index + 1][::-1]        
     
        return prefix + word[index + 1:]

        # Solution 1
        
        location = 0

        for i, v in enumerate(word):
            
            if v == ch:
                location = i
                break

        ans = word[0:location+1]
        ans = ans[::-1] + word[location+1::]

        return ans