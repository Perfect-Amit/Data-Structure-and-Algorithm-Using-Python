from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        Count = Counter(nums)
        res = 0
        for i in Count:
            if i+1 in Count:
                res= max(res, Count[i]+Count[i+1])
        return res