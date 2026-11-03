class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        nums.sort()
        for i in range(n):
            if nums[i] != nums[n-1]:
                total += nums[n-1] - nums[i]
            i += 1
        return total