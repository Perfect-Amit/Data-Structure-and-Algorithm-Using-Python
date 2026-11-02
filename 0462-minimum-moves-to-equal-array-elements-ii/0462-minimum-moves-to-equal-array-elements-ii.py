class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid=nums[len(nums)//2]
        count=0
        for x in nums:
            count+=abs(x-mid)
        return count