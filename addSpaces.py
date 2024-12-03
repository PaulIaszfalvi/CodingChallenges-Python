class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:

        # Solution 2

        parts = []
        prev_index = 0
        

        for space in spaces:
            parts.append(s[prev_index:space])
            prev_index = space

        parts.append(s[prev_index:])
 
        return " ".join(parts)



        # Solution 1
        
        answer = ""

        for i in range(len(spaces)):
            print(spaces[i])
            if i == 0:
                answer += s[0 : spaces[i]] + " "
            else:
                answer += s[spaces[i - 1] : spaces[i]] + " " 
                
        answer += s[spaces[-1] : ]

        return answer
