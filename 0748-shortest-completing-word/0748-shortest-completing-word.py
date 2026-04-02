class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        need = [0]*26
        for c in licensePlate:
            if c.isalpha():
                need[ord(c.lower()) - ord('a')] += 1
        ans = ""
        for w in words:
            have = [0]*26
            for c in w:
                have[ord(c) - ord('a')] += 1
            ok = True
            for i in range(26):
                if have[i] < need[i]:
                    ok = False
                    break
            if ok:
                if ans == "" or len(w) < len(ans):
                    ans = w
        return ans