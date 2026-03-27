class Solution:
    def applyOperations(self, nums):
        n=len(nums)
        
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        
        res=[]
        
        for num in nums:
            if num!=0:
                res.append(num)
        
        while len(res)<n:
            res.append(0)
        
        return res