class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d = {}
        ans = 0
        for x in range(lowLimit, highLimit + 1):
            s = 0
            n = x
            while n:
                s += n % 10
                n //= 10
            d[s] = d.get(s, 0) + 1
            if d[s] > ans:
                ans = d[s]
        return ans