class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n=len(s)
        cost=[[0]*n for _ in range(n)]

        divisors={}
        for length in range(2,n+1):
            divisors[length]=[d for d in range(1,length) if length%d==0]

        for length in range(2,n+1):
            for i in range(n-length+1):
                best=float('inf')
                for d in divisors[length]:
                    groups=length//d
                    changes=0

                    for r in range(d):
                        for t in range(groups//2):
                            if s[i+r+t*d]!=s[i+r+(groups-1-t)*d]:
                                changes+=1

                    best=min(best,changes)

                cost[i][i+length-1]=best

        dp=[[float('inf')]*(k+1) for _ in range(n+1)]
        dp[0][0]=0

        for p in range(1,k+1):
            for i in range(2*p,n+1):
                for j in range(2*(p-1),i-1):
                    dp[i][p]=min(
                        dp[i][p],
                        dp[j][p-1]+cost[j][i-1]
                    )

        return dp[n][k]