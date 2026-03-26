class Solution:
    def dominantIndex(self, nums):
        p = sorted(nums)
        n = len(nums)
        if p[n-1] >= 2 * p[n-2]:
            for i in range(n):
                if nums[i] == p[n-1]:
                    return i
        return -1