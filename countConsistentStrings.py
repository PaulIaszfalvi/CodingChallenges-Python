class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Convert the allowed string to a set for fast membership checking
        allowed_set = set(allowed)
        
        count = 0
        for word in words:
            # Check if every character in the word is in the allowed set
            if all(char in allowed_set for char in word):
                count += 1
                
        return count

      # Prototype

       # sets = []
       #  count = 0

       #  for x in words:
       #      sets.append(set(x))

       #  for x in sets:
       #      if len(x) > len(allowed):
       #          continue
       #      for y in allowed:
       #          if y in x:
       #              break
       #      print(x)
       #      count += 1

       #  return count
