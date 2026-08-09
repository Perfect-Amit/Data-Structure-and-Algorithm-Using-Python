class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for n in range(n, n + t):
            digits = list(map(int, str(n)))
            prod = 1
            for i in digits:
                prod = prod * i
            if prod % t == 0:
                return n
        return -1
        