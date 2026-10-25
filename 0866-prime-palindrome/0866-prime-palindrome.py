class Solution:
    def primePalindrome(self,n:int)->int:
        def is_prime(x):
            if x<2:
                return False
            if x%2==0:
                return x==2
            i=3
            while i*i<=x:
                if x%i==0:
                    return False
                i+=2
            return True
        if 8<=n<=11:
            return 11
        for length in range(1,10):
            half=(length+1)//2
            start=10**(half-1)
            end=10**half
            for x in range(start,end):
                s=str(x)
                pal=int(s+s[-2::-1] if length%2 else s[::-1]+s)
                if pal>=n and is_prime(pal):
                    return pal
        return -1