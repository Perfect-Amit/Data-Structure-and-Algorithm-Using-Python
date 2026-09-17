class Solution:
    def getSum(self,a:int,b:int)->int:
        m=0xffffffff
        n=0x7fffffff
        while b&m:
            c=(a&b)<<1
            a=(a^b)&m
            b=c
        return a if a<=n else ~(a^m)