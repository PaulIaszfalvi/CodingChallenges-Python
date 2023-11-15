class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):
        # One line
        # return reduce(lambda r, n: min(r + 1, n), sorted(arr)[1:], 1)

        # O(n) solution

        n = len(arr)
        count = [0] * (n + 1)  # Initialize a count array with size n + 1

        for num in arr:
            # Count the occurrences of each element up to n
            count[min(num, n)] += 1

        consecutive_count = 0
        for i in range(1, n + 1):
            # Update the consecutive_count to keep track of consecutive elements
            consecutive_count = min(consecutive_count + count[i], i)

        return consecutive_count

        #Faster Online 

        # arr.sort()
        # ans=1
        # for x in arr[1:]:
        #     ans=min(x, ans+1)
        # return ans
    
        #Solution 1

        # biggest = 1     

        # if arr[0] != 1:
        #     arr[0] = 1

        # for i in range(1, len(arr)):                        
        #     if abs(arr[i] - arr[i-1]) > 1:
        #         arr[i] = arr[i-1] + 1
        #     if biggest < arr[i]:
        #         biggest = arr[i]

        # return biggest 

arr = [2,2,1,2,1]
print(Solution().maximumElementAfterDecrementingAndRearranging(arr))