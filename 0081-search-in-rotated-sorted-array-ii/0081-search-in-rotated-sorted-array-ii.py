class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        k = 0
        while nums[k] != target:
            k += 1
            if k >= n:
                return False
        return True