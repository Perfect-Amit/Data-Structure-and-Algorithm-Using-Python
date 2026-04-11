class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo = {}
        
        def f(a, b):
            if a == b:
                return True
            
            if (a, b) in memo:
                return memo[(a, b)]
            
            if sorted(a) != sorted(b):
                return False
            
            n = len(a)
            
            for k in range(1, n):
                if (f(a[:k], b[:k]) and f(a[k:], b[k:])) or \
                   (f(a[:k], b[n-k:]) and f(a[k:], b[:n-k])):
                    memo[(a, b)] = True
                    return True
            
            memo[(a, b)] = False
            return False
        
        return f(s1, s2)