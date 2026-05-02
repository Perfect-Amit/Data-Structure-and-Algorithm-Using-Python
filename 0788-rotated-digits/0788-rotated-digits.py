class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for x in range(1, n + 1):
            num = x
            ok = True
            diff = False
            while num:
                d = num % 10
                if d in [3,4,7]:
                    ok = False
                    break
                if d in [2,5,6,9]:
                    diff = True
                num //= 10
            if ok and diff:
                ans += 1
        return ans