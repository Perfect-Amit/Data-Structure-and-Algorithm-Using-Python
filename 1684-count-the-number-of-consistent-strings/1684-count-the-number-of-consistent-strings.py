class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        st = set(allowed)
        ans = 0
        for w in words:
            ok = True
            for c in w:
                if c not in st:
                    ok = False
                    break
            if ok:
                ans += 1
        return ans