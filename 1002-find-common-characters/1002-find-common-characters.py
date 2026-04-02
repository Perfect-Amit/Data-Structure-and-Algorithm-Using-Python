class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        base = [0]*26
        for c in words[0]:
            base[ord(c)-97] += 1
        for w in words[1:]:
            cur = [0]*26
            for c in w:
                cur[ord(c)-97] += 1
            for i in range(26):
                base[i] = min(base[i], cur[i])
        res = []
        for i in range(26):
            res += [chr(i+97)] * base[i]
        return res