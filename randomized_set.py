class RandomizedSet:

    # Solution 1
    
    def __init__(self):
        self.s = set()        

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        else:
            self.s.add(val)     
            return True   

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        else:
            self.s.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice(list(self.s))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


# Absolute fastest with chatgpt Both are all O(1) with O(n) space complexity. This is faster because I don't have to convert the set to a list
    
# from collections import defaultdict
# from collections import deque
# import random

# class RandomizedSet:

    # def __init__(self):
    #     # Initialize a list to store elements
    #     self.lst = []
    #     # Initialize a defaultdict to store the index of each element in the list
    #     self.idx_map = defaultdict(int)

    # def search(self, val):
    #     # Check if the value exists in the index map
    #     return val in self.idx_map

    # def insert(self, val):
    #     # Check if the value already exists, return False if it does
    #     if self.search(val):
    #         return False

    #     # Append the value to the list
    #     self.lst.append(val)
    #     # Update the index map with the index of the new value
    #     self.idx_map[val] = len(self.lst) - 1
    #     return True

    # def remove(self, val):
    #     # Check if the value exists, return False if it doesn't
    #     if not self.search(val):
    #         return False

    #     # Get the index of the value to be removed
    #     idx = self.idx_map[val]
    #     # Swap the value with the last element in the list
    #     self.lst[idx] = self.lst[-1]
    #     # Update the index map for the swapped element
    #     self.idx_map[self.lst[-1]] = idx
    #     # Remove the last element using deque
    #     self.lst.pop()
    #     # Remove the value from the index map
    #     del self.idx_map[val]
    #     return True

    # def getRandom(self):
    #     # Return a random element from the list
    #     return random.choice(self.lst)
