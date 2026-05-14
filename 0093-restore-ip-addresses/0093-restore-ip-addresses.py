class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtrack(i, parts, path):
            if parts == 4 and i == len(s):
                res.append(".".join(path))
                return
            if parts == 4 or i == len(s):
                return
            for j in range(i, min(i + 3, len(s))):
                cur = s[i:j+1]
                if (cur[0] == '0' and len(cur) > 1) or int(cur) > 255:
                    continue
                path.append(cur)
                backtrack(j + 1, parts + 1, path)
                path.pop()
        backtrack(0, 0, [])
        return res