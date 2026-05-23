from collections import Counter
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        max_freq = max(freq.values())
        answer = 0
        for count in freq.values():
            if count == max_freq:
                answer += count
        return answer