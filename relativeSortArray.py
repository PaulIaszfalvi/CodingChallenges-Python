class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        # Solution 2
        counts = Counter(arr1)
        ans = []

        # Append elements from arr2
        for num in arr2:
            ans.extend([num] * counts[num])
            del counts[num]

        # Append remaining elements from arr1 in sorted order
        for num in sorted(counts):
            ans.extend([num] * counts[num])

        return ans

        # Solution 1
      
        a1 = dict(Counter(arr1))
        a2 = {i:v for i, v in enumerate(arr2)}
        ans = []

        for key, value in a2.items():
            ans += [value] * a1.get(value)
            del a1[value]
        
        a1 = {k: a1[k] for k in sorted(a1)}
       
        for key, value in a1.items():
            ans += [key] * value

        return ans
