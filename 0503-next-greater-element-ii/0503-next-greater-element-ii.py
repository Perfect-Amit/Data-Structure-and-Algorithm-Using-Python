class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        n=len(nums)
        res=[]
        for i in range(n):
            ans=-1
            for j in range(1,n):
                index=(i+j)%n
                if nums[index]>nums[i]:
                    ans=nums[index]
                    break
            res.append(ans)
        return res