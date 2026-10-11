class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        arr = []
        for i in range(n):
            if n % (i+1) == 0:
                arr.append(nums[i]**2)
        return sum(arr[:])