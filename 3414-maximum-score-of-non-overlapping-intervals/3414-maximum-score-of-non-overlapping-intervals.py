from bisect import bisect_left
class Solution:
    def maximumWeight(self,intervals:list[list[int]])->list[int]:
        arr=sorted((r,l,w,i) for i,(l,r,w) in enumerate(intervals))
        n=len(arr)
        ends=[x[0] for x in arr]
        prev=[]
        for i in range(n):
            l=arr[i][1]
            prev.append(bisect_left(ends,l,0,i)-1)
        dp=[[(0,()) for x in range(5)] for x in range(n+1)]
        for i in range(1,n+1):
            r,l,w,idx=arr[i-1]
            for k in range(1,5):
                skip=dp[i-1][k]
                p=prev[i-1]+1
                old=dp[p][k-1]
                chosen=tuple(sorted(old[1]+(idx,)))
                take=(old[0]+w,chosen)
                if take[0]>skip[0] or (take[0]==skip[0] and take[1]<skip[1]):
                    dp[i][k]=take
                else:
                    dp[i][k]=skip
        best=(0,())
        for k in range(1,5):
            cur=dp[n][k]
            if cur[0]>best[0] or (cur[0]==best[0] and cur[1]<best[1]):
                best=cur
        return list(best[1])