class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        a = []
        for i in range(n - 1):
            if nums[i + 1] == nums[i] + 1:
                continue
            else:
                for j in range(nums[i] + 1, nums[i + 1]):
                    a.append(j)
        return a