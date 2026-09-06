from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        count = Counter(arr)
        n = len(arr)
        for i in range(n):
            if count[arr[i]]/n*100 > 25:
                return arr[i]
