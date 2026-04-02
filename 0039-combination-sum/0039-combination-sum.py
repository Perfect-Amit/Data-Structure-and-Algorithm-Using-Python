class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if total > target:
                return
            for j in range(i, len(candidates)):
                cur.append(candidates[j])
                dfs(j, cur, total + candidates[j])
                cur.pop()
        dfs(0, [], 0)
        return res