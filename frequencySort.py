class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:

        # Solution 2
        
        frequency = Counter(nums)
        
        # Sort the items by frequency in ascending order, and by value in descending order in case of tie
        sorted_items = sorted(nums, key=lambda x: (frequency[x], -x))
        
        return sorted_items

      # Solution 1

        frequency = Counter(nums)
        
        # Sort the items by frequency, and by value in case of tie
        sorted_items = sorted(frequency.items(), key=lambda item: (item[1], item[0]))
        

        result = [key for key, count in sorted_items for _ in range(count)]
        
        return result

        
