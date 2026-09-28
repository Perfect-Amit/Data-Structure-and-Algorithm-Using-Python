class Solution:
    def maxDepth(self, s: str) -> int:
        arr = list(s)
        n = len(arr)
        i = 0
        count = 0
        res = 0
        while i < n:
            if arr[i] == '(':
                count += 1
                res = max(res, count)
                i += 1
            elif arr[i] == ')':
                count -= 1
                res = max(res, count)
                i += 1
            else:
                i += 1
        return res