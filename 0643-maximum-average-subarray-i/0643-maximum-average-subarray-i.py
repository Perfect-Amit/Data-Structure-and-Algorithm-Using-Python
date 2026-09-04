class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        if n==k:
            return sum(nums)/k
        Sum=0
        for i in range(k):
            Sum+=nums[i]
        i=k
        Max=Sum/k
        while i<n:
            Sum=Sum-nums[i-k]
            Sum=Sum+nums[i]
            Max=max(Max,Sum/k)
            i+=1
        return Max