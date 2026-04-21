from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1 = list(s1.split())
        s2 = list(s2.split())
        count1 = Counter(s1)
        count2 = Counter(s2)
        res = []
        for i in s1:
            if i in s2 or count1[i] > 1:
                continue
            else:
                res.append(i)
                continue
        for j in s2:
            if j in s1 or count2[j] > 1:
                continue
            else:
                res.append(j)
        return res