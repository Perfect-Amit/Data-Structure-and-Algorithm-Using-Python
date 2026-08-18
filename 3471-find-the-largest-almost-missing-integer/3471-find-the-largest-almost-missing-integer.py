from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = Counter()
        for i in range(len(nums) - k + 1):
            for x in set(nums[i:i+k]):
                freq[x] += 1
        return max((x for x in freq if freq[x] == 1), default=-1)