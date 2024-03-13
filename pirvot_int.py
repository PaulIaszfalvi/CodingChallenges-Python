class Solution:
    def pivotInteger(self, n: int) -> int:

        # Solution 3 O(1)

        sum = n * (n + 1) // 2
        
        # Check if the sum is a perfect square
        root = int(sum ** 0.5)
        if root * root == sum:
            return root
        else:
            return -1
    
        # Solution 2 Big O(logn) or O(log log n)

        x = sqrt(n * (n + 1) / 2)

        if x % 1 != 0:
            return -1
        else:
            return int(x)

        # Solution 1 Big O(n)
        
        l = int(n*(n+1)/2)
        r = n

        print(l)

        while l >= r:
            if l == r:
                return n
            
            l -= n
            n -= 1
            r += n
          
        return -1
