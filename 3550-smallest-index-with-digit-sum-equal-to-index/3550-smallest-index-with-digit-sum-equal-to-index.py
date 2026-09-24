class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            x = str(nums[i])
            for j in x:
                y = list(x)
                z = sum(int(k) for k in y)
            if z == i:
                return i
        return -1