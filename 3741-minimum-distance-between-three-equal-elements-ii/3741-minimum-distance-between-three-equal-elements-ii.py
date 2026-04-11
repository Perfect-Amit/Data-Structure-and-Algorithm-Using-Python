class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        pos = {}
        for i, x in enumerate(nums):
            if x not in pos:
                pos[x] = []
            pos[x].append(i)
        ans = float('inf')
        for v in pos.values():
            if len(v) < 3:
                continue
            for i in range(len(v) - 2):
                d = 2 * (v[i+2] - v[i])
                ans = min(ans, d)
        return ans if ans != float('inf') else -1