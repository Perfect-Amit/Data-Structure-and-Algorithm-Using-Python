class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        mod1=10**9+7
        mod2=10**9+9
        base1=100003
        base2=100019

        p1=[1]*(n+1)
        p2=[1]*(n+1)
        h1=[0]*(n+1)
        h2=[0]*(n+1)

        for i in range(n):
            p1[i+1]=p1[i]*base1%mod1
            p2[i+1]=p2[i]*base2%mod2
            h1[i+1]=(h1[i]*base1+nums[i])%mod1
            h2[i+1]=(h2[i]*base2+nums[i])%mod2

        def check(length):
            freq={}
            unique=0

            for i in range(n-length+1):
                a=(h1[i+length]-h1[i]*p1[length])%mod1
                b=(h2[i+length]-h2[i]*p2[length])%mod2
                key=(a,b)

                count=freq.get(key,0)

                if count==0:
                    unique+=1
                elif count==1:
                    unique-=1

                freq[key]=count+1

            return unique>0

        left=1
        right=n

        while left<right:
            mid=(left+right)//2

            if check(mid):
                right=mid
            else:
                left=mid+1

        return left