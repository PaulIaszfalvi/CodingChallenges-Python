class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:

      # Solution 3

        if not meetings:
            return days  # If no meetings, all days are free

        meetings.sort()
        merged = [meetings[0]]

        for start, end in meetings[1:]:
            last_start, last_end = merged[-1]
            if start <= last_end:  # Merge overlapping or adjacent intervals
                merged[-1][1] = max(last_end, end)
            else:
                merged.append([start, end])

        # Count free days
        ans = merged[0][0] - 1  # Days before the first meeting
        ans += days - merged[-1][1]  # Days after the last meeting

        for i in range(1, len(merged)):
            ans += merged[i][0] - merged[i-1][1] - 1  # Days between meetings
        
        return ans



      # Solution 2 (Doesn't take overlapping arrays into account)

      ans = 0

        for x in meetings:
            ans += x[1] - x[0] + 1

        print(days, ans)

        return days - ans

      # Solution 1 (TLE)
        
        s = set()

        for i in meetings:
            for j in range(i[0], i[1]+1):
                s.add(j)

        return days - len(s)
