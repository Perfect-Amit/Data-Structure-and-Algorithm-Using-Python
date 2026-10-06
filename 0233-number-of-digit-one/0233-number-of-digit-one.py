class Solution:
    def countDigitOne(self, n: int) -> int:
        ans=0
        factor=1
        while factor<=n:
            high=n//(factor*10)
            cur=(n//factor)%10
            low=n%factor
            if cur==0:
                ans+=high*factor
            elif cur==1:
                ans+=high*factor+low+1
            else:
                ans+=(high+1)*factor
            factor*=10
        return ans