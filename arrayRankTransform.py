
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        # Solution 2

        # Step 1: Create a sorted list of unique elements
        unique_sorted = sorted(set(arr))
        
        # Step 2: Map each unique element to its rank
        rank_map = {val: idx + 1 for idx, val in enumerate(unique_sorted)}
        
        # Step 3: Replace elements in the original array with their ranks
        return [rank_map[x] for x in arr]

        # Solution 1

        # Sort the array to determine the ranks
        s_arr = sorted(arr)
        d = {}
        c = 1

        # Assign ranks to each element
        for x in s_arr:
            if x not in d:  # Only assign rank if x is not already ranked
                d[x] = c
                c += 1

        # Transform the original array to its rank representation
        for i in range(len(arr)):
            arr[i] = d[arr[i]]

        return arr
