class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left = sum(int(x) for x in num[:n//2] if x != '?')
        right = sum(int(x) for x in num[n//2:] if x != '?')
        lq = num[:n//2].count('?')
        rq = num[n//2:].count('?')
        if abs(lq - rq) % 2:
            return True
        return left - right != (rq - lq) * 9 // 2