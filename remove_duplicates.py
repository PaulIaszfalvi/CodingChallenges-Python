class Solution:
    def removeDuplicates(self, nums) -> int:

        unique = 1
        #fast = 1

        if len(nums) <= 1:
            return len(nums)
        
        # while fast < len(nums)-1:

        #     while nums[slow] == nums[fast]:
        #         nums[fast] = "_"
        #         fast += 1

        #     slow += 1
        #     fast += 1
        #     nums[slow] = nums[fast]
        #     nums[fast] = "_"

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique] = nums[i]                
                unique += 1
            else:
                nums[i] = None

       
        return unique, nums

nums = [1,1,2,2,3]
print(Solution().removeDuplicates(nums))