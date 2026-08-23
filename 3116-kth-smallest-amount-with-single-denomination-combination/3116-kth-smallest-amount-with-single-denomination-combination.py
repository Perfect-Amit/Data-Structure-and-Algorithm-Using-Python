from math import gcd
from functools import reduce
class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        def lcm(a, b):
            return a // gcd(a, b) * b
        def count(x):
            ans = 0
            for mask in range(1, 1 << len(coins)):
                multiple = 1
                bits = 0
                for i in range(len(coins)):
                    if mask & (1 << i):
                        multiple = lcm(multiple, coins[i])
                        bits += 1
                if multiple > x:
                    continue
                if bits % 2:
                    ans += x // multiple
                else:
                    ans -= x // multiple
            return ans
        left = 1
        right = min(coins) * k
        while left < right:
            mid = (left + right) // 2
            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1
        return left