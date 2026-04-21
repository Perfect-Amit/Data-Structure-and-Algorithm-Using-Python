class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        a = sorted(set(arr))
        rank = {}
        r = 1
        for v in a:
            rank[v] = r
            r += 1
        res = []
        for x in arr:
            res.append(rank[x])
        return res