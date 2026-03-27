from collections import Counter
class Solution:
    def relativeSortArray(self, arr1, arr2):
        count=Counter(arr1)
        res=[]
        for x in arr2:
            res.extend([x]*count[x])
            count[x]=0
        remaining=[]
        for x in count:
            remaining.extend([x]*count[x])
        remaining.sort()
        return res+remaining