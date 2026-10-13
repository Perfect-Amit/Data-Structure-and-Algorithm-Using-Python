class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x:x*x)
        n=len(nums)
        half=n//2
        return sum(x*x for x in nums[half:])-sum(x*x for x in nums[:half])