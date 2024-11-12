from typing import List
from bisect import bisect_left

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        # Solution 3

        maxI = float('inf')
        res = [[0, 0, maxI]]
    
        items.sort(key=lambda x: x[0])

        for price, beauty in items:
            lastBracket = res[-1]
            if beauty > lastBracket[1]:
                res[-1][2] = price
                res.append([price, beauty, maxI])

        ans = []

        for x in queries:
            for i in range(len(res) - 1, -1, -1):
                if res[i][0] <= x:
                    ans.append(res[i][1])
                    break

        return ans

        # Solution 2 (TLE)

        # Step 1: Sort items by price
        items.sort()
        
        # Step 2: Precompute maximum beauty for each price threshold
        max_beauty = []
        current_max = 0
        for price, beauty in items:
            current_max = max(current_max, beauty)
            max_beauty.append((price, current_max))
        
        # Step 3: Sort queries with their original indices to restore order later
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        
        # Step 4: Result array to store the answers in the original order of queries
        result = [0] * len(queries)
        
        # Step 5: Process each query
        for q, original_index in sorted_queries:
            # Find the rightmost price that is <= q
            idx = bisect_right([price for price, _ in max_beauty], q) - 1
            
            if idx >= 0:
                result[original_index] = max_beauty[idx][1]
            else:
                result[original_index] = 0  # No items are affordable for this query price
        
        return result



      # Solution 1 (TLE)
        
        def create_special_hashmap(pairs):
            hashmap = {}
            
            for key, value in pairs:
                # Step 1: Update if the key already exists and has a lower value
                if key in hashmap:
                    hashmap[key] = max(hashmap[key], value)
                else:
                    # Step 2: Find the maximum value among all smaller keys
                    max_smaller_value = max((v for k, v in hashmap.items() if k < key), default=None)
                    
                    # Step 3: Decide the value to store based on the exception condition
                    if max_smaller_value is not None and value < max_smaller_value:
                        hashmap[key] = max_smaller_value
                    else:
                        hashmap[key] = value
            
            return hashmap

        # Step 4: Create the hashmap from items
        csh = create_special_hashmap(items)
        
        # Step 5: Sort keys and update cumulative max values
        sorted_keys = sorted(csh.keys())
        cumulative_max = {}
        max_value = 0  # Start with 0 as default if no valid key is found
        for key in sorted_keys:
            max_value = max(max_value, csh[key])
            cumulative_max[key] = max_value
        
        # Step 6: Process each query using the cumulative max
        ans = []
        for i in queries:
            # Find the index of the closest lower key
            idx = bisect_left(sorted_keys, i)
            if idx == 0:
                # All keys are larger than the query; return 0 if no suitable key exists
                ans.append(0 if sorted_keys[0] > i else cumulative_max[sorted_keys[0]])
            elif idx == len(sorted_keys) or sorted_keys[idx] > i:
                # idx is beyond last key or greater than i, use nearest smaller key
                ans.append(cumulative_max[sorted_keys[idx - 1]])
            else:
                # Exact match
                ans.append(cumulative_max[sorted_keys[idx]])

        return ans
