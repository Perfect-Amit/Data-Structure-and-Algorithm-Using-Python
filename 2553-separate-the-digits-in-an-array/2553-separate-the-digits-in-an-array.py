class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        res=[]
        for num in nums:
            x=str(num)
            for k in x:
                res.append(int(k))
        return res