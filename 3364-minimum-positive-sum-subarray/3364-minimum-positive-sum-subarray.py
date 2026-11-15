class Solution:
    def minimumSumSubarray(self,nums: list[int],l: int,r: int) -> int:
        n=len(nums)
        prefix=[0]*(n+1)
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]
        res=float('inf')
        for i in range(n):
            for length in range(l,r+1):
                j=i+length
                if j<=n:
                    total=prefix[j]-prefix[i]
                    if total>0:
                        res=min(res,total)
        return res if res!=float('inf') else -1