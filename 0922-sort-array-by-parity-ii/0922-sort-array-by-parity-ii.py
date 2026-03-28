class Solution:
    def sortArrayByParityII(self, nums):
        n=len(nums)
        arr1=[]
        arr2=[]
        res=[0]*n
        for i in range(n):
            if nums[i]%2==0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        i=0
        for x in arr1:
            res[i]=x
            i+=2
        i=1
        for x in arr2:
            res[i]=x
            i+=2
        return res