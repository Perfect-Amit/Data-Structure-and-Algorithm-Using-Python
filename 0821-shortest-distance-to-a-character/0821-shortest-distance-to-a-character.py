class Solution:
    def shortestToChar(self, s, c):
        n=len(s)
        res=[0]*n
        prev=float('-inf')
        for i in range(n):
            if s[i]==c:
                prev=i
            res[i]=i-prev
        prev=float('inf')
        for i in range(n-1,-1,-1):
            if s[i]==c:
                prev=i
            res[i]=min(res[i],prev-i)
        return res