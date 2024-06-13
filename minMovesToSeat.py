class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:

        # Solution 2 

        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))

        # Solution 1
        
        se = {i:k for k, i in enumerate(seats)}
        st = {i:k for k, i in enumerate(students)}

        st = dict(sorted(st.items()))
        se = dict(sorted(se.items()))

        ans = 0

        for a, b in zip(st, se):
            ans += abs(st[a] - se[b])

        return ans
