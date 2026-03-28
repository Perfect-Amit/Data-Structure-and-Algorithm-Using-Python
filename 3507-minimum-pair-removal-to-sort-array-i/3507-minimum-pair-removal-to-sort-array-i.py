class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(arr):
            for i in range(len(arr)-1):
                if arr[i] > arr[i+1]:
                    return False
            return True
        ops=0
        while not is_sorted(nums):
            n=len(nums)
            min_sum=float('inf')
            idx=0
            for i in range(n-1):
                s=nums[i]+nums[i+1]
                if s<min_sum:
                    min_sum=s
                    idx=i
            nums=nums[:idx]+[min_sum]+nums[idx+2:]
            ops+=1
        return ops