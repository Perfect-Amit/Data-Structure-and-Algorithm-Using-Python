class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ins_score = []
        for i in range(n):
            ins_score.append(max(nums[0:i+1])-min(nums[i:n]))
        for j in range(n):
            if ins_score[j] <= k:
                return j
        return -1