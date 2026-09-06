class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected_height = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != expected_height[i]:
                res += 1
        return res