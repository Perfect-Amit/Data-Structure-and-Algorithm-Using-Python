from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        count=Counter(s)
        length=0
        odd=False

        for c in count.values():
            length+=c//2*2
            if c%2==1:
                odd=True

        if odd:
            length+=1

        return length