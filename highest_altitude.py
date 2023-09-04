class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        maximum = 0
        altitude = 0

        for a in gain:
            altitude += a
            maximum = max(maximum, altitude)

        return maximum


gain = [0, 5, -5, -7, 1, 0, 7, -10]
print(Solution().largestAltitude(gain))