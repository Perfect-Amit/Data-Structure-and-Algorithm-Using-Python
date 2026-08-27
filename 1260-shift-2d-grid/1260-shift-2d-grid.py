class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        total = m * n
        k %= total
        ans = [[0] * n for k in range(m)]
        for i in range(m):
            for j in range(n):
                pos = (i * n + j + k) % total
                ans[pos // n][pos % n] = grid[i][j]
        return ans