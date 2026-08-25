class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)
        j = 1
        while j * k in nums:
            j += 1
        return j * k