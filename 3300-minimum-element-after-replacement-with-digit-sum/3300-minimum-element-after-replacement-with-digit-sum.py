class Solution:
    def minElement(self, nums: List[int]) -> int:
        n = len(nums)
        Sum = 0 
        res = float('Inf')
        for i in range(n):
            x = str(nums[i])
            for j in range(len(x)):
                Sum += nums[i]%10
                nums[i] //= 10
            res = min(res, Sum)
            Sum = 0
        return res