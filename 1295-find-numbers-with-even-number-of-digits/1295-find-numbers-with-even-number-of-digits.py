class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        n = len(nums)
        st = ''
        count = 0
        for i in nums:
            st = str(i)
            if len(st) % 2 ==0:
                count += 1
            st = ''
        return count