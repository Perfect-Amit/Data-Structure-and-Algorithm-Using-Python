class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        m = len(set(candyType))
        if m >= n // 2:
            return n // 2
        else:
            return m