from collections import Counter
class Solution:
    def getHint(self,secret:str,guess:str)->str:
        bulls=0
        s=Counter()
        g=Counter()
        for i in range(len(secret)):
            if secret[i]==guess[i]:
                bulls+=1
            else:
                s[secret[i]]+=1
                g[guess[i]]+=1
        cows=0
        for digit in s:
            cows+=min(s[digit],g[digit])
        return str(bulls)+'A'+str(cows)+'B'