class Solution:
    def maxNumOfSubstrings(self,s:str)->list[str]:
        first={}
        last={}
        for i,ch in enumerate(s):
            if ch not in first:
                first[ch]=i
            last[ch]=i
        intervals=[]
        for ch in first:
            l=first[ch]
            r=last[ch]
            i=l
            valid=True
            while i<=r:
                if first[s[i]]<l:
                    valid=False
                    break
                r=max(r,last[s[i]])
                i+=1
            if valid:
                intervals.append((l,r))
        intervals.sort(key=lambda x:x[1])
        res=[]
        end=-1
        for l,r in intervals:
            if l>end:
                res.append(s[l:r+1])
                end=r
        return res