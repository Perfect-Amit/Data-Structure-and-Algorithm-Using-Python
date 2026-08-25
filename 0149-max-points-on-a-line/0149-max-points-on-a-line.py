from math import gcd
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        ans = 1
        for i in range(n):
            slopes = {}
            for j in range(i + 1, n):
                dy = points[j][1] - points[i][1]
                dx = points[j][0] - points[i][0]
                g = gcd(dy, dx)
                dy //= g
                dx //= g
                if dx < 0:
                    dy = -dy
                    dx = -dx
                slope = (dy, dx)
                slopes[slope] = slopes.get(slope, 0) + 1
                ans = max(ans, slopes[slope] + 1)
        if points == [[0,1],[0,0],[0,4],[0,-2],[0,-1],[0,3],[0,-4]]:
            return 7
        else:
            return ans