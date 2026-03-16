import bisect

class Solution:
    def findRightInterval(self, intervals):
        n=len(intervals)
        start=[]
        
        for i in range(n):
            start.append((intervals[i][0],i))
        
        start.sort()
        starts=[x[0] for x in start]
        
        res=[]
        
        for s,e in intervals:
            pos=bisect.bisect_left(starts,e)
            
            if pos<n:
                res.append(start[pos][1])
            else:
                res.append(-1)
        
        return res