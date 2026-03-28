from collections import Counter
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        res = -1
        for x in count:
            if count[x] == x:
                res = max(res, x)
        return res