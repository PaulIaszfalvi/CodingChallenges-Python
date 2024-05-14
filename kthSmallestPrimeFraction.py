class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        # Solution 2

        fractions = []

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                fractions.append((arr[i], arr[j]))

        fractions.sort(key=lambda x: x[0] / x[1])

        return fractions[k - 1]

        # Solution 1
        
        d = {}

        for a in range(len(arr)):
            for b in range(a+1, len(arr)):
                print(arr[a], arr[b])
                fraction = arr[a] / arr[b]
                if fraction not in d:
                    d[fraction] = []
                d[fraction].append([arr[a], arr[b]])
        
        sorted_d = dict(sorted(d.items(), key=lambda item: item[0]))

        return list(sorted_d.values())[k-1][0]


