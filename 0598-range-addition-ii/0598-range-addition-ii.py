class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        r = m
        c = n
        for a, b in ops:
            r = min(r, a)
            c = min(c, b)
        return r * c