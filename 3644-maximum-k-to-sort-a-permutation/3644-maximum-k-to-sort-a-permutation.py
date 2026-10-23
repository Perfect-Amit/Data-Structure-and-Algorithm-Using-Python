class Solution:
    def sortPermutation(self,nums:list[int])->int:
        n=len(nums)
        if nums==list(range(n)):
            return 0
        k=(1<<30)-1
        for i,x in enumerate(nums):
            if x!=i:
                k&=x&i
        return k