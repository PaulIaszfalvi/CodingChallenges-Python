class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        



        # Bad description example solution 

        l = len(arr)
        arr.sort()
        print(arr)
        ans = []

        remainder = l % k

        for x in range(l//k):
            pop = arr.pop()
            ans.append(pop * k)
            print(arr)

        if remainder != 0:
            ans.append(arr.pop()* remainder)

        print(ans)

        return sum(ans)