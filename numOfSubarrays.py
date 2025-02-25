class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        n = len(arr)
        ans = 0

        for i in range(n):
            for j in range(i, n):
                subarray = arr[i:j+1]  
                if sum(subarray) % 2 == 1: 
                    ans += 1

        return ans


      # Better online solution

        odd_count = 0
        even_count = 1  # We start with 1 because an empty prefix sum is even
        prefix_sum = 0
        ans = 0
        MOD = 10**9 + 7  # To avoid large numbers

        for num in arr:
            prefix_sum += num  # Update prefix sum
            
            if prefix_sum % 2 == 1:
                ans += even_count  # Odd prefix sum means it can pair with previous even subarrays
                odd_count += 1  # Increase odd count
            else:
                ans += odd_count  # Even prefix sum means it can pair with previous odd subarrays
                even_count += 1  # Increase even count
            
            ans %= MOD  # Keep the result within bounds

        return ans

