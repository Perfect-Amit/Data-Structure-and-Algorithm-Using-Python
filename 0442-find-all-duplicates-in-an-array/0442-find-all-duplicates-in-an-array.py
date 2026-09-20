class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        n = len(nums)
        res = []
        for i in range(n):
            if count[nums[i]] > 1:
                if nums[i] not in res:
                    res.append(nums[i])
        return res