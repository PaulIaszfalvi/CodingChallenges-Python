class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #5700-6000ms

        numSet = set(nums)
        longest = 0

        for x in nums:
            if (x-1) not in numSet:
                length = 0
                while (x+length) in numSet:
                    length += 1
                longest = max(length, longest)              
       
        return longest
    
    # Better online literally same thing at 350ms

        # if not nums:
        #     return 0

        # num_set = set(nums)
        # longest_streak = 0

        # for num in num_set:
        #     if num - 1 not in num_set:
        #         current_num = num
        #         current_streak = 1

        #         while current_num + 1 in num_set:
        #             current_num += 1
        #             current_streak += 1

        #         longest_streak = max(longest_streak, current_streak)

        # return longest_streak
