class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        s = list(s)
        res = -1
        for i in range(len(s)):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    new_res = j - (i+1)
                    res = max(res, new_res)
        return res