class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff=[abs(a-b) for a,b in zip(nums1,nums2)]
        k=k1+k2
        if sum(diff)<=k:
            return 0
        left=0
        right=max(diff)
        while left<right:
            mid=(left+right)//2
            needed=sum(max(0,d-mid) for d in diff)
            if needed<=k:
                right=mid
            else:
                left=mid+1
        level=left
        needed=sum(max(0,d-level) for d in diff)
        remaining=k-needed
        ans=0
        for d in diff:
            value=min(d,level)
            if value==level and remaining>0:
                value-=1
                remaining-=1
            ans+=value*value
        return ans