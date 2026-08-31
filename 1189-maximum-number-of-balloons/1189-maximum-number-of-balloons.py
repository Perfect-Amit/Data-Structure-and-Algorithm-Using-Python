class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b_count = 0
        a_count = 0
        l_count = 0
        o_count = 0
        n_count = 0
        for ch in text:
            if ch=='b':
                b_count+=1
            elif ch=='a':
                a_count+=1
            elif ch=='l':
                l_count+=1
            elif ch=='o':
                o_count+=1
            elif ch=='n':
                n_count+=1
        return min(b_count,a_count,l_count//2,o_count//2,n_count)