class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # Solution 3

        # Convert integers to strings
        array = list(map(str, nums))
        
        # Custom sorting with a lambda function
        array.sort(key=lambda x: x*10, reverse=True)
        
        # Handle the case where the largest number is "0"
        if array[0] == "0":
            return "0"
        
        # Build the largest number from the sorted array
        largest = ''.join(array)
        
        return largest

        # Solution 2

        # Custom comparison function
        def compare(x, y):
            # Compare concatenated strings
            if x + y > y + x:
                return -1  # x should come before y
            else:
                return 1   # y should come before x

        # Convert integers to strings
        str_nums = list(map(str, nums))
        
        # Sort using the custom comparator
        sorted_nums = sorted(str_nums, key=cmp_to_key(compare))
        
        # Join sorted numbers into a single string
        ans = ''.join(sorted_nums)
        
        # Edge case: if the result is all zeros
        return ans if ans[0] != '0' else '0'



        # Solution 1

        def custom_sort(numbers):
            # Sort by last digit (as second key), then by first digit (as first key)
            return sorted(numbers, key=lambda x: (x % 10, x // 10), reverse=True)
        
        ans = ''
        
        for x in custom_sort(nums):
            ans += str(x)

        return ans
