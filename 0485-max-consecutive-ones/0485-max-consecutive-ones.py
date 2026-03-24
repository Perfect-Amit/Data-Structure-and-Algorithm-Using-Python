class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        maximum = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 1:
                res += 1
            else:
                maximum = max(maximum,res)
                res = 0
        maximum = max(maximum,res)
        return maximum