class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        count = Counter(nums)
        res = []
        for i in range(len(nums)):
            if count[nums[i]] == 1:
                if nums[i] not in res:
                    res.append(nums[i])
        return res