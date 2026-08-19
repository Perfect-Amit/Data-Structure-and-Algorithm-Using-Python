class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        rows = {}
        for r, s in reservedSeats:
            rows.setdefault(r, set()).add(s)
        ans = (n - len(rows)) * 2
        for seats in rows.values():
            left = not any(x in seats for x in [2, 3, 4, 5])
            middle = not any(x in seats for x in [4, 5, 6, 7])
            right = not any(x in seats for x in [6, 7, 8, 9])
            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1
        return ans