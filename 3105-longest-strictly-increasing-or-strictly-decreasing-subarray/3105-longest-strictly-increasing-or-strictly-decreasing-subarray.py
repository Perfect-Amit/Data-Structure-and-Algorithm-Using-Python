class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        count_inc = 1
        count_dec = 1
        temp = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                count_inc += 1
                count_dec = 1
            elif nums[i] < nums[i-1]:
                count_dec += 1
                count_inc = 1
            else:
                count_inc = 1
                count_dec = 1
            temp=max(count_inc, count_dec, temp)
        return temp