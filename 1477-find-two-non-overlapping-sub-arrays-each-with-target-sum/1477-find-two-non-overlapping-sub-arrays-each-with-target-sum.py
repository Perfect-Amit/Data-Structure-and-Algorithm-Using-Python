class Solution:
    def minSumOfLengths(self,arr:list[int],target:int)->int:
        n=len(arr)
        best=[float('inf')]*n
        prefix=0
        seen={0:-1}
        ans=float('inf')
        for i,x in enumerate(arr):
            prefix+=x
            if i>0:
                best[i]=best[i-1]
            if prefix-target in seen:
                j=seen[prefix-target]
                length=i-j
                if j>=0 and best[j]!=float('inf'):
                    ans=min(ans,length+best[j])
                best[i]=min(best[i],length)
            seen[prefix]=i
        return -1 if ans==float('inf') else ans