class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        inc = sorted(nums)
        dec = sorted(nums, reverse=True)
        if nums == inc or nums == dec:
            return True
        return False