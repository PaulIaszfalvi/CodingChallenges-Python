from itertools import product
class Solution:
    def letterCombinations(self, digits: str):
        
        if digits == "":
            return []
        
        number_list = [["a", "b", "c"], 
                       ["d", "e", "f"],
                       ["g", "h", "i"],
                       ["j", "k", "l"],
                       ["m", "n", "o"],
                       ["p", "q", "r", "s"],
                       ["t", "u", "v"],
                       ["w", "x", "y", "z"]]

        result = []
        combinations = []
        
        for n in digits:
            combinations.append(number_list[int(n)-2])
        
        for combination in combinations:
            result =  [f"{x}{y}" for x in result for y in combination if x != "" or y != ""] if result else combination

        return result


digits = ""
print(Solution().letterCombinations(digits))

digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(Solution().letterCombinations(digits))

