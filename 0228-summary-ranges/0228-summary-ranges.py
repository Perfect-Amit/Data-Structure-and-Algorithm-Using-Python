class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0
        n = len(nums)
        while i < n:
            st = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if st == nums[i]:
                res.append(str(st))
            else:
                res.append(str(st) + "->" + str(nums[i]))
            i += 1
        return res