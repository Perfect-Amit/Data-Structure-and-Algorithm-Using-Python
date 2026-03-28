class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        res2 = []
        for i in range(n):
            if nums[i] % 2 == 0:
                res.append(nums[i])
            else:
                res2.append(nums[i])
        res.extend(res2)
        return res