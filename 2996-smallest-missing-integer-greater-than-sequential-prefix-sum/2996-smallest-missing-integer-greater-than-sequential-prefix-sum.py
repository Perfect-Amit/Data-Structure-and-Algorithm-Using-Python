class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        s = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                break
            s += nums[i]
        nums_set = set(nums)
        while s in nums_set:
            s += 1
        return s