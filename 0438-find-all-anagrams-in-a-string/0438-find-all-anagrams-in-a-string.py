from collections import Counter
class Solution:
    def findAnagrams(self,s:str,p:str)->list[int]:
        n=len(s)
        m=len(p)
        target=Counter(p)
        window=Counter()
        res=[]
        for i in range(n):
            window[s[i]]+=1
            if i>=m:
                window[s[i-m]]-=1
                if window[s[i-m]]==0:
                    del window[s[i-m]]
            if i>=m-1 and window==target:
                res.append(i-m+1)
        return res