from collections import Counter

class Solution:
    def frequencySort(self, s):
        freq=Counter(s)
        
        res=[]
        for ch,count in sorted(freq.items(), key=lambda x: -x[1]):
            res.append(ch*count)
        
        return ''.join(res)