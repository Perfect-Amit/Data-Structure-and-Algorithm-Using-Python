class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n=len(nums)
        total=sum(nums)
        current=sum(i*x for i,x in enumerate(nums))
        ans=current
        for i in range(n-1,0,-1):
            current=current+total-n*nums[i]
            ans=max(ans,current)
        return ans