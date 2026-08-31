class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def helper(arr):
            prev=0
            curr=0
            for money in arr:
                prev,curr=curr,max(curr,prev+money)
            return curr
        return max(helper(nums[:-1]),helper(nums[1:]))