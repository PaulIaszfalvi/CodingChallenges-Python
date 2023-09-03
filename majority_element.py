class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        map = {}
        max_value = nums[0]
        
        for e in nums:            
            map[e] = map.get(e, 0) +1
        
        for key, value in map.items():
            max_value = key if value > map.get(max_value) else max_value
         
        return max_value
    

    # Faster solution

    #nums.sort()
    #return nums[len(nums)//2]

    #From what I gather from this problem, the majority number will always take up half or more of the list of numbers. When the list is sorted, the majority number will be either on the left or the right, but definitely in the middle. Once the list is sorted, len(nums)//2 will find the middle term (rounded down), and we just return that term by the index we just calculated.