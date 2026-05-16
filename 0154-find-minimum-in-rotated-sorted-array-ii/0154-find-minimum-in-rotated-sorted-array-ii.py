class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        nums2 = sorted(nums)
        if nums2 == nums:
            return nums[0]
        else:
            for i in range(n-1):
                if nums[i] > nums[i+1]:
                    return nums[i+1]