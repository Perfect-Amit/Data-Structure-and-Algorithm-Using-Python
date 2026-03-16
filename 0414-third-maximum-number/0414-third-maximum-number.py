class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if len(nums) >= 3:
            return nums[len(nums)-3]
        else:
            if len(nums) == 0:
                return 0
            elif len(nums) == 1:
                return nums[0]
            else:
                return nums[1]